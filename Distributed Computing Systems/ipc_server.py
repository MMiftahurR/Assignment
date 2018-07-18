# Import library
import socket
from threading import Thread
import json
import time

def handle_thread(conn):
    while True :
        try :
            # Terima data dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            json_data = json.loads(data)
            print("data didapat pada ",time.clock())
            print("Temperature\t= ",json_data["Temperature"], " K")
            print("Kelembapan\t= ",json_data["Kelembapan"], " %")
            print("Oksigen\t\t= ",json_data["Oksigen"], " %")
            print("------------------------------------------------------")
            reply = "OK"
            conn.send( reply.encode('ascii') ) 
        except(socket.error):
            # Tangkap error dari koneksi
            print("Koneksi ditutup oleh client")
            # Tutup koneksi
            conn.close()
            break
            

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ikat process server ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )

# Listen
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Buat thread baru setiap ada permintaan koneksi
    t=Thread(target=handle_thread, args=(conn,))
    # Start thread baru
    t.start()
    