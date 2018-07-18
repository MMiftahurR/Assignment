from flask import Flask, request
import json

app = Flask("Web App Mahasiswa")

data_mahasiswa = [
    {
        "nim" : 123,
        "nama" : "Andi"
    },
    {
        "nim" : 234,
        "nama" : "Budi"
    }
]

@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    json_mahasiswa = json.dumps(data_mahasiswa)
    return json_mahasiswa

@app.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    # Dapatkan data nim dan nama dari body request
    nim = request.json['nim']
    nama = request.json['nama']
    # Buat data mahasiswa baru
    mahasiswa_baru = {
        "nim" : nim,
        "nama" : nama
    }
    # Tambahkan ke list data mahasiswa
    data_mahasiswa.append(mahasiswa_baru)
    # Return OK
    return "OK"

@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_satu_mahasiswa(id):
    return str(id)


app.run(port=7777)