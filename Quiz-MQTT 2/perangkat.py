import paho.mqtt.client as mqtt_client

pub = mqtt_client.Client()
pub.connect("127.0.0.1",1883)

pub.publish("/sensor/suhu", "30")
pub.publish("/sensor/humidity", "80%")
pub.publish("/sensor/co2", "20%")