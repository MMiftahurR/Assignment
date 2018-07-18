#instal bson dulu, lalu pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient() #bisa berparameter domain dan port tujuan
db = client.test
collection = db.inventory

#update
'''
filter_document = {
    "_id" : ObjectId("5afd153f55227f10bc28f56c")
}
set_new_document = {
    "$set": {
        "name": "agus a"
    }
}
#upsert = False, jika tidak ditemukan dokumen, akan dibuat dokumen baru
#multi = True, untuk meng-update banyak dokumen
result = collection.update(filter_document, set_new_document, upsert=False, multi=True)
print(result)
'''

#insert one
'''
new_document = {
    "name": "Suga",
    "age": 20,
    "address": ["sidorahayu", "malang"],
    "item": "anyone"
}
collection.insert_one(new_document)
'''

#insert many
'''
new_documents = [
    {
        "a": 1,
        "b": 2
    },{
        "c": 3,
        "d": 4
    }
]
collection.insert_many(new_documents)
'''

#delete one
'''
delete_document = {
    "a": 1,
    "b": 2
}
collection.delete_one(delete_document)
'''

#delete many
'''
delete_document = {
    "a": 1,
    "b": 2
}
collection.delete_many(delete_document)
'''

#find one
'''
document = collection.find_one({"_id" : ObjectId("5afd153f55227f10bc28f56c")})
print(document)
'''

#find all
'''
documents = collection.find({})
for document in documents:
    print(document)
'''