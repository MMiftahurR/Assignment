#instal bson dulu, lalu pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from flask import Flask, request, jsonify

app = Flask("WEBSERVICE DB to APP")

client = MongoClient() #bisa berparameter domain dan port tujuan
db = client.skt #nama db
collection = db.sensor2 #inventory adalah nama tabel

@app.route('/data', methods=['GET'])
def find_all():
	data = []
	documents = collection.find({})
	for doc in documents:
		data.append({'id_device' : doc['id_device'],
        't_total' : doc['t_total'],
        't_sampah' : doc['t_sampah'],
        'persentase' : doc['persentase'],
        'timestamp' : str(doc['timestamp'])})
	return jsonify(data)

app.run(host='0.0.0.0', port=7777)
