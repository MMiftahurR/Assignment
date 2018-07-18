#!/usr/bin/python3
# Import library socket
import socket
from threading import Thread
import sys
import json

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
username = sys.argv[2]

def handle_thread(conn):
    while True :
        try :
            data = conn.recv(100)
            data = data.decode('ascii')
            data, sender = data.split(" Sender ")
            print('\n------------------------INBOX--------------------------')
            print('dapat pesan dari {}'.format(sender))
            print('pesan\t: '+data)
            print('------------------------RESUME-------------------------')
        except(socket.error):
            # Tangkap error dari koneksi
            print("Koneksi ditutup")
            # Tutup koneksi
            conn.close()
            break

# Inisiasi object socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
confirm = 'N'

# Inisiasi 3-way handshaking/bikin koneksi
tcp_sock.connect(srv_sockaddr)
print('Client has been assigned socket name', tcp_sock.getsockname())

new_msg = {'command':'INISIASI','pesan':'save username','tujuan':'server','sender':username}
payload = json.dumps(new_msg).encode('utf-8')
tcp_sock.send(payload)

t=Thread(target=handle_thread, args=(tcp_sock,))
# Start thread baru
t.start()
print('================================================================')
while confirm == 'N':
    command = input()
    if command.upper() != 'CLOSE' : 
        if command.upper() == 'BROADCAST':
            data = input('Masukkan Pesan\t\t:')
            new_msg = {'command':command.upper(),'pesan':data,'tujuan':'all','sender':username}
            print('Mengirim pesan "'+ data +'" secara broadcast')
            payload = json.dumps(new_msg).encode('utf-8')
            tcp_sock.send(payload)
        elif command.upper() == 'PERSONAL':
            data = input('Masukkan Pesan\t\t:')
            penerima = input('Username Reciever\t:')
            print('Mengirim pesan "'+ data +'" ke '+penerima)
            new_msg = {'command':command.upper(),'pesan':data,'tujuan':penerima,'sender':username}
            payload = json.dumps(new_msg).encode('utf-8')
            tcp_sock.send(payload)
        else:
            print('Error:Command not found')
    else:
        confirm = input('Apakah anda ingin mengakhiri Sesi? (Y/N)\t: ').upper()
    print('================================================================')
# Tutup koneksi
tcp_sock.close()