#!/usr/bin/python3 

import sys
import socket
from time import gmtime, strftime
import signal

def listen():
    srv_ip, srv_port = sys.argv[1].split(":")
    srv_sockaddr = (srv_ip, int(srv_port))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(srv_sockaddr)
    print("Press Crtl+c to exit...") 

    #while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        payload, cln_sockaddr = sock.recvfrom(1480)
        payloadrep = ""
            
        quet = payload.decode()
        print('Receive question "{}"'.format(quet))
        if quet == "jam berapa?":
            payloadrep = strftime("%H:%M:%S", gmtime()).encode('ascii')
        elif quet == "tanggal berapa?": 
            payloadrep = strftime("%Y-%m-%d", gmtime()).encode('ascii')
        else:
            payloadrep = ("Query tidak dikenali").encode('ascii')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(payloadrep, cln_sockaddr)
        listen()
    except KeyboardInterrupt:
        sys.exit()
        
listen()
