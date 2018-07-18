#!/usr/bin/python3
# Program TCP client
# author: mahendra.data@ub.ac.id

import sys
import socket

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(srv_sockaddr)
print('Client has been assigned socket name', sock.getsockname())
sock.sendall('Hi there, server'.encode('ascii'))
reply = sock.recv(16)
print('The server said', reply.decode('ascii'))
sock.close()