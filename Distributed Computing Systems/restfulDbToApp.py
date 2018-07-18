#instal bson dulu, lalu pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from flask import Flask, request

app = Flask("WEBSERVICE DB to APP")

client = MongoClient() #bisa berparameter domain dan port tujuan
db = client.skt #nama db
collection = db.sensor2 #inventory adalah nama tabel

@app.route('/data', methods=['GET'])
def find_all():
	list = []
	documents = collection.find({})
	for doc in documents:
		list.append(str(doc))
	return json.dumps(list)

app.run(host='0.0.0.0', port=7777)