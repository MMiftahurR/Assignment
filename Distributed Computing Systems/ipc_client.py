# Import library
import socket
import random
import sys
import time
import json

# Inisiasi object socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking/bikin koneksi
tcp_sock.connect( ("127.0.0.1", 6667) )

#for i in range(0,3):
i = 1
while True:
    raw_data = [random.randint(273,373), random.randint(0,100), random.randint(0,100)]
    # Kirim data
    data = {"Temperature": str(raw_data[0]), "Kelembapan": str(raw_data[1]), "Oksigen": str(raw_data[2])}
    tcp_sock.send( json.dumps(data).encode('ascii') )
    print("data ke-",(i)," dikirim pada",time.clock()," ,value data : ",data)
    # Terima data
    i += 1
    time.sleep(1)
    data = tcp_sock.recv(100)
    data = data.decode('ascii')
    print(data)
