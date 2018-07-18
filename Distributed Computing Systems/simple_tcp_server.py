# Import library socket
import socket

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ikat process server ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )

# Listen
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Terima data dari client
    data = conn.recv(100)
    data = data.decode('ascii')
    data = "OK "+data
    # Kirim balik ke client
    conn.send( data.encode('ascii') )
    # Tutup koneksi
    #conn.close()