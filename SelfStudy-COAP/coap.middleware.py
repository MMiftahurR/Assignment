from flask import Flask, request
from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683

app = Flask("SMART HOME")


@app.route('/home/<app>/<payload>', methods=['POST'])
def app_invoked(payload,app):
    client = HelperClient(server=(host, port))
    path = app+"/"
    print(path)
    print(payload)
    response = client.post(path,payload)
    rep = response.payload
    client.stop()
    return rep

try:
    app.run(port=7777)
except KeyboardInterrupt:
    print("Server Shutdown")
    app.shutdown()
    print("Exiting...")