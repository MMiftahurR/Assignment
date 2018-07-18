from coapthon.client.helperclient import HelperClient

host = "127.0.0.1"
port = 5683
path ="app1"

client = HelperClient(server=(host, port))
resp = client.get(path)
print(resp.payload)
client.stop()