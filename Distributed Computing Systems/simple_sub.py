import paho.mqtt.client as mqtt_client
import sys

sub = "/home/"+sys.argv[1]
sub = mqtt_client.Client()
sub.connect("127.0.0.1", 1883)
print("Subscribe pada\t",sub)
sub.subscribe(sub)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode("ascii")
    print("Topik : ",topic,"\t, Payload : ",payload)
    print("Perangkat\t:",sys.argv[1])
    print(payload)

sub.on_message = handle_message
sub.loop_forever()