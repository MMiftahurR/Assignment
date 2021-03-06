#!/usr/bin/python3
# Program RTT Server Select
# author: mahendra.data@ub.ac.id
# execute: ./code5.4.py <IP>:<PORT>
import select
import signal
import socket
import sys
srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setblocking(0)
serversock.bind(srv_sockaddr)
serversock.listen(1)
rlist = [serversock]
print('Listening at', serversock.getsockname())
print("Press Crtl+c to exit...")
while True:
    try:
        signal.signal(signal.SIGINT, signal.default_int_handler)
        readable, _, _ = select.select(rlist, [], [])
        for s in readable:
            if s is serversock:
                datasock, clientsockaddr = serversock.accept()
                print('datasock\t: {}'.format(datasock.getpeername()))
                print('clientsockaddr\t: {}'.format(clientsockaddr))
                datasock.setblocking(0)
                rlist.append(datasock)
                print('Client {} connected'.format(clientsockaddr))
            else:
                data = s.recv(2048)
                print(s.getpeername())
                if data:
                    s.sendall(data)
                else:
                    rlist.remove(s)
                    print('Client {} disconnected'.format(s.getpeername()))
                    s.close()
    except KeyboardInterrupt:
        break
serversock.close()