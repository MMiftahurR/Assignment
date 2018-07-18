# Import lib paho mqtt
import paho.mqtt.client as mqtt_client

# Initialize mqtt client for doctor
doctor = mqtt_client.Client()

# Connect to broker
doctor.connect("127.0.0.1", port=1883)

def case(inp):
    if(inp <= 180):
        return "Jika anda masih 2 jam setelah makan, anda normal, jika tidak, segera ke puskesmas terdekat"
    else:
        return "Segara kunjungi dokter terdekat"
    
# Message handle
def handle_message(client, object, message):
    print("Topic\t: " + message.topic)
    print("Message\t: " + message.payload.decode('ascii'))
    # Publish message topic
    rep = case(int(message.payload.decode('ascii')))
    doctor.publish("/saran", rep.encode('ascii'))

# Register function for message handler
doctor.on_message = handle_message

# Subscribe to topic
doctor.subscribe("/kadar")

# Loop forever (handle subscribe)
doctor.loop_forever()