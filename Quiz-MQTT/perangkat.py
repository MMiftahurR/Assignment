import paho.mqtt.client as mqtt_client
import sys

topic = "/home/"+sys.argv[1]+"/#"
sub = mqtt_client.Client()
sub.connect("127.0.0.1", 1883)
print("Subscribe pada\t",topic)
sub.subscribe(topic)

def handle_message(mqttc, obj, msg):
    topic = msg.topic
    payload = msg.payload.decode("ascii")
    print("Topik : ",topic,"\t, Payload : ",payload)
    print("Perangkat\t:",sys.argv[1])
    print("Status\t\t:",payload)

sub.on_message = handle_message
sub.loop_forever()