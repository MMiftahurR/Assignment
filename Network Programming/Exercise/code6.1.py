#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.1.py <IP>:<PORT> <DATA>
import socket
import sys
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_sockaddr)
payload, cln_sockaddr = sock.recvfrom(2048)
print('Payload length: {}'.format(len(payload)))
print('Data: {}'.format(payload.decode(sys.argv[2])))
sock.close()