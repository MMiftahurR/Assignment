#!/usr/bin/python3
# Program Data Encoding
# author: mahendra.data@ub.ac.id
# execute: ./code6.4.py <IP>:<PORT>
import socket
import sys
import struct
def send(fmt, *data):
    payload = struct.pack(fmt, *data)
    sock.sendto(payload, srv_sockaddr)
    
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send("!h", 128)
send("!i", 1234567890)
send("!f", 1234.5)
send("!d", 12345.6789)
send("!hifd", 128, 1234567890, 1234.5, 12345.6789)
sock.close()