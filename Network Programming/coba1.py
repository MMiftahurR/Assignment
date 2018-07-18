from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import xmlrpc.server

client = MongoClient() #bisa berparameter domain dan port tujuan
db = client.skt
collection = db.sensor2
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

def getDataDevice():
    documents = collection.find({})
    for document in documents:
        if document['id_device'] == "1":
            temp1 = document
        elif document['id_device'] == "2":
            temp2 = document
        data = []
        data.append[dict(temp1)]
        data.append[dict(temp2)]
        return json.dumps(data)
        
#operasi = (data1['t_sampah']/data1['t_total'])*100

def updateDb(data):
    filter_document = {
        "_id" : ObjectId(str(data['_id']))
    }
    set_new_document = {
        "$set": {
            "persentase": data["operasi"]
        }
    }
    result = collection.update(filter_document, set_new_document, upsert=False, multi=True)
    return json.dumps(result)

def cekData():
    documents = collection.find({})
    for document in documents:
        if document['id_device'] == "1":
            temp1 = document
        elif document['id_device'] == "2":
            temp2 = document
    print(temp1)
    print(temp2)

server.register_function(getDataDevice, "getDataDevice")
server.register_function(updateDb, "updateDb")
server.register_function(cekData, "cekData")
server.serve_forever()