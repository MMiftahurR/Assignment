#!/usr/bin/python3
# Program RTT client
# author: mahendra.data@ub.ac.id
# execute: ./code5.2.py <IP>:<PORT> <COUNT>

import threading
import socket
import sys
import time
import signal

class Receive(threading.Thread):
    threadCount = 0

    def __init__(self, clientsock, sendSock):
        threading.Thread.__init__(self)
        self.clientsock = clientsock
        self.sendSock = sendSock
        Receive.threadCount += 1
        self._is_running = True

    def stop(self):
        self._is_running = False
    
    def run(self):
        while True:
        
            pesan = self.clientsock.recv(2048)
            pesan = pesan.decode()
            pesan = pesan.split()
        
            asal = pesan.pop()
            asal = asal.split(':')
        
            asal[1] = int(asal[1])
            for i in self.sendSock:
                if pesan and tuple(asal) in self.sendSock:
                    print('Pesan terkirim-> "'+ ' '.join(pesan)+'"')
                    #self.clientsock.close()            
                    #Receive.threadCount -= 1
                    #sys.exit()
                else:
                    print('Menerima pesan baru dari server-> "'+ ' '.join(pesan)+'"')
                    #self.clientsock.close()            
                    #Receive.threadCount -= 1
                    #sys.exit()

class Send(threading.Thread):
    threadCount = 0
    def __init__(self, clientsock):
        threading.Thread.__init__(self)
        self.clientsock = clientsock
        Send.threadCount += 1
        self._is_running = True

    def stop(self):
        self._is_running = False
    
    def run(self):
        while True:
            ip_address, port = self.clientsock.getsockname()
            
            pesan = input().encode() 
            print('Mengirim pesan "'+ pesan.decode()+'" ke server')
            self.clientsock.sendto(pesan, (ip_address, int(port)))
            
            #self.clientsock.close()
            #Send.threadCount -= 1
            #sys.exit()           

srv_ip, srv_port = sys.argv[1].split(":")
srv_sockaddr = (srv_ip, int(srv_port))

threadDict = {}
sendSocket = []
receiveThreadCount = 0

while True:
    try:    
        if(Send.threadCount == 0):
            #receiveThreadCount += 1

            clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsock.connect(srv_sockaddr)
            sendSocket.append(clientsock.getsockname())
            print('Client has been assigned socket name', clientsock.getsockname())
    
            signal.signal(signal.SIGINT, signal.default_int_handler)
            sendingThread = Send(clientsock)
            #threadDict[clientsock.getsockname()] = sendingThread
            sendingThread.start() 
        else:
            continue
        
        if(Receive.threadCount == 0):
            clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            clientsock.connect(srv_sockaddr)
            print('Client has been assigned socket name', clientsock.getsockname())
    
            signal.signal(signal.SIGINT, signal.default_int_handler)
            receivingThread = Receive(clientsock, sendSocket)
            threadDict[clientsock.getsockname()] = receivingThread
            #for _ in sendSocket:
            #   print('sendSocket: '+str(_))
            receivingThread.start() 
        else:
            continue
    
    except KeyboardInterrupt:
        print("Waiting client threads...")            
        for thread in threadDict.values():
            thread.join()
        break
    except socket.timeout:
        clientsock.close()


#while True:
    #try:
#clientsock.send(b'Test!')
#reply = clientsock.recv(2048)
 
#if reply:
#    print(repr(reply))
    #except socket.timeout:
    #    clientsock.close()

for _ in threadDict:
    print(_)

clientsock.close()
