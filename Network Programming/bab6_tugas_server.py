#!/usr/bin/python3
# Program RTT Server Select
# author: mahendra.data@ub.ac.id
# execute: ./code5.4.py <IP>:<PORT>
import select
import signal
import socket
import sys
import json

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setblocking(0)
serversock.bind(srv_sockaddr)
serversock.listen(1)
rlist = [serversock]
userlist = {}

def broadcast(sender,pesan):
    print('Broadcast Pesan')
    for client in rlist:
        if client != serversock:
            if sender != client.getpeername():
                target_address, target_port = client.getpeername() 
                client.send(pesan.encode('ascii'))

def personal(sender,pesan,reciever):
    for client in rlist:
        if client != serversock:
            try:
                if userlist[reciever] == client.getpeername():
                    target_address, target_port = client.getpeername()
                    print(sender+' Mengirim pesan ke '+reciever)
                    client.send(pesan.encode('ascii'))
                    break
            except:
                print('Penerima tidak ada')
                break
                
print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        readable, _, _ = select.select(rlist, [], [])
        for s in readable:
            if s is serversock:
                datasock, clientsockaddr = serversock.accept()
                datasock.setblocking(0)
                rlist.append(datasock)
                print('Client {} connected'.format(clientsockaddr))
            else:
                data = s.recv(2048)
                if data:
                    payload = json.loads(data.decode('utf-8'))
                    if payload['command'].upper() == 'INISIASI':
                        username = payload['sender']
                        peer = s.getpeername()
                        userlist[username] = peer
                        print('Client {} username {} '.format(peer,username))
                    elif payload['command'].upper() == 'BROADCAST':
                        sender = payload['sender']
                        pesan = payload['pesan'] + ' Sender ' + sender
                        peersender = s.getpeername()
                        broadcast(peersender,pesan)
                    elif payload['command'].upper() == 'PERSONAL':
                        sender = payload['sender']
                        pesan = payload['pesan'] + ' Sender ' + sender
                        reciever = payload['tujuan']
                        personal(sender,pesan,reciever)
                else:
                    rlist.remove(s)
                    print('Client {} disconnected'.format(s.getpeername()))
                    s.close()
    except KeyboardInterrupt:
        break
serversock.close()