# Import library xmlrpc
import xmlrpc.client
import sys

# Inisiasi proxy ke server
proxy = xmlrpc.client.ServerProxy("http://localhost:7778/")
NamaSensor = sys.argv[1]
hasil1 = proxy.getALL()
print("get ALL : ")
print(hasil1)
print("get Sensor : ")
hasil2 = proxy.getSensor(NamaSensor)
print(hasil2)