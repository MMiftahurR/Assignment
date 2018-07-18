#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.6.py <IP>:<PORT>
import socket
import sys
import pickle
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data1 = pickle.dumps({1:"satu", 2:2.0, 3:3})
data2 = pickle.dumps([4,5,6])
print("data1: ", data1)
print("data2: ", data2)
payload1 = data1+data2[:3]
payload2 = data2[3:]
print("payload1: ", payload1)
print("payload2: ", payload2)
# simulasi dua buah paket datang disaat hampir bersamaan,
# sehingga perintah recv akan membaca sebagian payload2
sock.sendto(payload1, srv_sockaddr)
sock.sendto(payload2, srv_sockaddr)
sock.close()
