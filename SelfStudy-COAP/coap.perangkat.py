from coapthon.client.helperclient import HelperClient
import sys
import time

host,port = sys.argv[1].split(':') 
path =sys.argv[2] +"/"
try:
    while True:
        client = HelperClient(server=(host, id(port)))
        resp = client.get(path)
        print(sys.argv[2]+" "+resp.payload)
        client.stop()
        time.sleep(60)
except KeyboardInterrupt:
    client.stop()
    print("Exiting...")