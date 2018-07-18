import paho.mqtt.client as mqtt_client
import sys
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient() #bisa berparameter domain dan port tujuan
db = client.test #test adalah nama db
collection = db.inventory #inventory adalah nama tabel

ip,port = sys.argv[1].split(':')
topic = sys.argv[2]
sub = mqtt_client.Client()
sub.connect(ip, int(port))
print("Subscribe pada\t",topic)
sub.subscribe(topic)

def insert(payload):
    new_document = payload
    collection.insert_one(new_document)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    insert(payload)

sub.on_message = handle_message
sub.loop_forever()