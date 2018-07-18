#!/usr/bin/python3
# Program TCP server
# author: mahendra.data@ub.ac.id

import sys
import socket
import signal

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(srv_sockaddr)
sock.listen(1)
print('Listening at', sock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        sc, sockname = sock.accept()
        print('We have accepted a connection from', sockname)
        print(' Socket name:', sc.getsockname())
        print(' Socket peer:', sc.getpeername())
        message = sc.recv(16)
        print(' Incoming sixteen-octet message:', repr(message))
        sc.sendall('Farewell, client'.encode('ascii'))
        sc.close()
        print(' Reply sent, socket closed')
    except KeyboardInterrupt:
        break