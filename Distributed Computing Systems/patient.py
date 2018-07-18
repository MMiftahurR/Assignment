# Import lib paho mqtt
import paho.mqtt.client as mqtt_client
import time

# Initialize mqtt client for patient
patient = mqtt_client.Client()

# Connect to broker
patient.connect("127.0.0.1", port=1883)

# Message handle
def handle_message(client, object, message):
    print("Topic\t: " + message.topic)
    print("Message\t: " + message.payload.decode('ascii'))

# Register function for message handler
patient.on_message = handle_message

# Subscribe to topic
patient.subscribe("/saran")

# Loop (handle subscribe)
patient.loop_start()

# Input data
data = int(input("Input kadar gula anda (mg/L)\t: "))
if(data > 120):
    # Publish message topic
    patient.publish("/kadar", data)
    time.sleep(1)