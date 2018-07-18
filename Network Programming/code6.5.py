#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.5.py <IP>:<PORT>
import socket
import sys
import pickle
def read(payload):
    data = pickle.loads(payload)
    return data, payload[payload.find(b".")+1:]

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(srv_sockaddr)
payload, cln_sockaddr = sock.recvfrom(2048)
data, buffer = read(payload)
print(data)
print(buffer)
payload, cln_sockaddr = sock.recvfrom(2048)
payload = buffer + payload
data, buffer = read(payload)
print(data)
print(buffer)
sock.close()