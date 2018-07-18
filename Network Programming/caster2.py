#!/usr/bin/python3
import socket
import struct
import sys

group, sender_port = sys.argv[1].split(':')
msg = sys.argv[2]
group_multicast = (group, int(sender_port))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

try:
    # Send data to the multicast group
    print('sending {!r}'.format(msg))
    sent = sock.sendto(msg.encode('ascii'), group_multicast)

    # Look for responses from all recipients
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received {!r} from {}'.format(data.decode(), server))

finally:
    print('closing socket')
    sock.close()
