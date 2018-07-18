#!/usr/bin/python3 
import sys
import socket

srv_ip, srv_port = sys.argv[1].split(":")
msg = sys.argv[2]
srv_sockaddr, payload = (srv_ip, int(srv_port)), msg.encode('ascii')

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #Untuk Broadcast
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
    sock.sendto(payload, srv_sockaddr)

    payloadb, sender = sock.recvfrom(1480)
    print('Receive "{}" from {}'.format(payloadb, sender))
except socket.error:
    print("Socket Error. Mengakhiri program..")
    sys.exit()
