import http.client
import time
import sys
ip_server = "127.0.0.1"
port_server = 7777

def nyala(par):
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    url = "/home/"+ par +"/nyala"
    print(url)
    conn.request("POST", url )
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)
    
def mati(par):
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    url = "/home/"+ par +"/mati"
    print(url)
    conn.request("POST", url )
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

mati(sys.argv[1])