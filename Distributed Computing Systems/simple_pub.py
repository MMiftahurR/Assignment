import paho.mqtt.client as mqtt_client
import time
import json

pub = mqtt_client.Client()
pub.connect("broker.hivemq.com",1883)

for i in range(10):
    new_json = {'id':'1','value':50,'lokasi':'Test'}
    pub.publish("/skt2/test", json.dumps(new_json).encode())
    time.sleep(2)