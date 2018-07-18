from flask import Flask, request
import paho.mqtt.client as mqtt_client

klien = mqtt_client.Client()
klien.connect("127.0.0.1", port=1883)

app = Flask("SMART HOME")


@app.route('/home/kulkas/<int:id>', methods=['POST'])
def kulkas_invoked(id):
    payload = "Error"
    if(id==0):
        payload = "Mati"
    elif(id==1):
        payload = "Menyala"
    topik = "/home/kulkas/"
    klien.publish(topik,payload.encode('ascii'))
    rep = "OK published as "+topik
    return rep

@app.route('/home/kipas/<int:id>', methods=['POST'])
def kipas_invoked(id):
    payload = "Error"
    if(id==0):
        payload = "Mati"
    elif(id==1):
        payload = "Menyala"
    topik = "/home/kipas/"
    klien.publish(topik,payload.encode('ascii'))
    rep = "OK published as "+topik
    return rep

@app.route('/home/lampu/<int:id>', methods=['POST'])
def lampu_invoked(id):
    payload = "Error"
    if(id==0):
        payload = "Mati"
    elif(id==1):
        payload = "Menyala"
    topik = "/home/lampu/"
    klien.publish(topik,payload.encode('ascii'))
    rep = "OK published as "+topik
    return rep

app.run(port=7777)