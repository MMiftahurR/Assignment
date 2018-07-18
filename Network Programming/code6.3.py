#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.3.py <IP>:<PORT>
import socket
import sys
import struct
def recv(fmt, payload):
    print('Payload: {}'.format(payload))
    print('Payload length: {} bytes'.format(len(payload)))
    print('Data: {}\n'.format(struct.unpack(fmt, payload)))
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_sockaddr)
payload, cln_sockaddr = sock.recvfrom(2048)
recv("!h", payload)
payload, cln_sockaddr = sock.recvfrom(2048)
recv("!i", payload)
payload, cln_sockaddr = sock.recvfrom(2048)
recv("!f", payload)
payload, cln_sockaddr = sock.recvfrom(2048)
recv("!d", payload)
payload, cln_sockaddr = sock.recvfrom(2048)
recv("!hifd", payload)
sock.close()