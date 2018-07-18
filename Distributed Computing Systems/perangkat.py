import paho.mqtt.client as mqtt_client
import sys
import json

dataset = []
ip,port = sys.argv[1].split(':')
topic = sys.argv[2]
sub = mqtt_client.Client()
sub.connect(ip, int(port))
print("Subscribe pada\t",topic)
sub.subscribe(topic)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode("ascii")
    dataset.append(payload)

def getData():
    return json.dumps(dataset)
    
sub.on_message = handle_message
sub.loop_forever()