import http.client

ip_server = "127.0.0.1"
port_server = 7777

def get_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Kirim request ke server
    conn.request("GET", "/mahasiswa")
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

def add_mahasiswa():
    conn = http.client.HTTPConnection(ip_server, port=port_server)
    # Definisi headers HTTP
    header = {"Content-Type" : "application/json"}
    # Definisikan data yang akan ditambahkan
    mhs = {
        "nim" : 910,
        "nama" : "Eka"
    }
    json_mhs = json.dumps(mhs)
    # Kirim request POST /mahasiswa dengan body dan header
    conn.request("POST", "/mahasiswa", json_mhs, header)
    # Baca responsenya
    data = conn.getresponse().read()
    data = data.decode('ascii')
    print(data)

#Panggil fungsi
add_mahasiswa()
get_mahasiswa()
