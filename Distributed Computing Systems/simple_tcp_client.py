# Import library socket
import socket

# Inisiasi object socket
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Inisiasi 3-way handshaking/bikin koneksi
tcp_sock.connect( ("127.0.0.1", 6667) )

# Kirim data
data = "Hello"
tcp_sock.send( data.encode('ascii') )

# Terima data
data = tcp_sock.recv(100)
data = data.decode('ascii')
print(data)

# Tutup koneksi
tcp_sock.close()