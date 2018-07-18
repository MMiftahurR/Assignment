from flask import flask, request
import json

app = flask("Web App Mahasiswa")

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

@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
	nim = request.json['nim']
	nama = request.json['nama']
	mahasiswa_baru = {
		"nim" : nim,
		"nama": nama
	}
	data_mahasiswa.append(mahasiswa_baru)
	json_mahasiswa = json.dumps(data_mahasiswa)
	return json_mahasiswa

@app.route('/mahasiswa', methods=['GET'])
def edit_mahasiswa():
	nim = request.json['nim']
	nama = request.json['nama']
	mahasiswa_baru = {
		"nim" : nim,
		"nama": nama
	}
	pass

@app.route('/mahasiswa/', methods=['GET'])
def delete_mahasiswa():
	nim = request.json['nim']
	nama = request.json['nama']
	mahasiswa_baru = {
		"nim" : nim,
		"nama": nama
	}
	pass

@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    json_mahasiswa = json.dumps(data_mahasiswa)
    return json_mahasiswa

@app.route('/mahasiswa/<int:id>', methods=['GET'])
def get_one_student(id):
	# Teko tek e agus 
	"""
	mhs1 = data_mahasiswa
	for mhs in mahasiswa:
	if(mhs.get("nim") == id):
			mhs1 = mhs
			break
	json_mahasiswa = json.dumps(mhs1)
	return json_mahasiswa
	"""
app.run(port=7777)