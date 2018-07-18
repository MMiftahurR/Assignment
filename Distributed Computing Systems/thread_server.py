# Import library socket
import socket
from threading import Thread

def handle_thread(conn):
    while True :
        try :
            # Terima data dari client
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send( data.encode('ascii') )            
        except(socket.error):
            # Tangkap error dari koneksi
            print("Koneksi ditutup oleh client")
            # Tutup koneksi
            conn.close()
            break
            

# Inisiasi objek socket TCP/IPv4
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ikat process server ke IP dan port tertentu
tcp_sock.bind( ("0.0.0.0", 6667) )

# Listen
tcp_sock.listen(100)

while True :
    # Terima permintaan koneksi dari client
    conn, client_addr = tcp_sock.accept()
    # Buat thread baru setiap ada permintaan koneksi
    t=Thread(target=handle_thread, args=(conn,))
    # Start thread baru
    t.start()
    