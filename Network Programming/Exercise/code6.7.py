#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.7.py <IP>:<PORT>
import socket
import sys
import json
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_sockaddr)
payload, cln_sockaddr = sock.recvfrom(2048)
sock.close()
data = json.loads(payload.decode('utf-8'))
sum = 0
for i in data:
    sum += i
print("Data: ", data)
print("Sum: ", sum)

