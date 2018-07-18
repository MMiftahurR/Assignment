#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.2.py <IP>:<PORT> <ENCODING> <DATA>
import socket
import sys
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = sys.argv[3]
payload = data.encode(sys.argv[2])
sock.sendto(payload, srv_sockaddr)
sock.close()
