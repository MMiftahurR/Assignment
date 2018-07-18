import paho.mqtt.client as mqtt_client
import sys
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
#Running ./sensorToDb.py [alamat]:[port] [topik]

client = MongoClient('mongodb://192.168.56.121') #bisa berparameter domain dan port tujuan
db = client.skt #adalah nama db
collection = db.sensor2 # adalah nama tabel
client1 = MongoClient('mongodb://192.168.56.122') #bisa berparameter domain dan port tujuan
db1 = client1.skt #adalah nama db
collection1 = db1.sensor2 # adalah nama tabel
client2 = MongoClient('mongodb://127.0.0.1') #bisa berparameter domain dan port tujuan
db2 = client2.skt #adalah nama db
collection2 = db2.sensor2 # adalah nama tabel

ip,port = sys.argv[1].split(':')
topic = sys.argv[2]
sub = mqtt_client.Client()
sub.connect(ip, int(port))
print("Subscribe pada\t",topic)
sub.subscribe(topic)

def insert(payload):
	new_document = payload
	collection.insert_one(new_document)
	collection1.insert_one(new_document)
	collection2.insert_one(new_document)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = json.loads(msg.payload)
    insert(payload)

sub.on_message = handle_message
sub.loop_forever()