#!/usr/bin/python3
import socket
import struct
import sys

mcast_group, mcast_port = sys.argv[1].split(":")
server = ('',int(mcast_port))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server)
mreq = struct.pack("4sl", socket.inet_aton(mcast_group), socket.INADDR_ANY)

# Receive/respond loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1480)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)
    print(data.decode('ascii'))

    print('sending acknowledgement to', address)
    sock.sendto(b'ack', address)