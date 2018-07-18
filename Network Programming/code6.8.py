#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.8.py <IP>:<PORT>
import socket
import sys
import json
import random
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = [random.randint(1, 100) for _ in range(10)]
payload = json.dumps(data).encode('utf-8')
sock.sendto(payload, srv_sockaddr)
sock.close()
