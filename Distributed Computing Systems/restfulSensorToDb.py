import paho.mqtt.client as mqtt_client
import sys
import json
from flask import Flask, request
import time
from threading import Thread
#Running ./sensorToDb.py [alamat]:[port] [topik]

app = Flask("SMART TRASHCAN")

dataset = []
ip,port = sys.argv[1].split(':')
topic = sys.argv[2]
sub = mqtt_client.Client()
sub.connect(ip, int(port))
print("Subscribe pada\t",topic)
sub.subscribe(topic)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    dataset.append(payload)

@app.route('/dataset', methods=['GET'])
def getData():
    return json.dumps(dataset)

def handle_thread():
    sub.on_message = handle_message
    sub.loop_forever()

def handle_thread2():
    app.run(host='0.0.0.0', port=7777)

t=Thread(target=handle_thread, args=())
# Start thread baru
t.start()
t2=Thread(target=handle_thread2, args=())
# Start thread baru
t2.start()
