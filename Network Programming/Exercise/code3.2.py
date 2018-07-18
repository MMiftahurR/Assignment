#!/usr/bin/python3

import sys
import socket

srv_ip, srv_port = sys.argv[1].split(":")
msg = sys.argv[2]
srv_sockaddr, payload = (srv_ip, int(srv_port)) , msg.encode("ascii")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(payload, srv_sockaddr)
