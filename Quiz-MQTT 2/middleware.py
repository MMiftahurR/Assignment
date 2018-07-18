# Import library xmlrpc
import xmlrpc.server
import json
import paho.mqtt.client as mqtt_client
from threading import Thread

sub = mqtt_client.Client()
sub.connect("127.0.0.1", port=1883)
sub.subscribe("/sensor/#")

# Inisiasi server
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )
data_sensor = []

# Definisi procedure atau fungsi
def getALL():
    json_sensor = json.dumps(data_sensor)
    return json_sensor

def getSensor(par):
    temp = []
    for i in data_sensor:
        if(i["sensor"] == par):
            temp.append(i)
    json_sensor = json.dumps(temp)
    return json_sensor

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode("ascii")
    sensor = topic.replace("/sensor/","")
    print("Sensor : ",sensor,"\t, Payload : ",payload)
    data_baru = {
        "sensor" : sensor,
        "data" : payload
    }
    data_sensor.append(data_baru)

def handle_thread():
    sub.on_message = handle_message
    sub.loop_forever()

# register fungsinya
server.register_function(getALL, "getALL")
server.register_function(getSensor, "getSensor")
t=Thread(target=handle_thread, args=())
# Start thread baru
t.start()

# Running server RPC
server.serve_forever()
