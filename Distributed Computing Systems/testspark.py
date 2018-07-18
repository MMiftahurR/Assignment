# Import library xmlrpc
import xmlrpc.client
import pyspark
import json

# Inisiasi proxy ke server
#proxy = xmlrpc.client.ServerProxy("http://[IP coba1.py]:7778/")

sc = SparkContext.getOrCreate()
#data = proxy.getDataDevice()
data = [{"id_device":1,"t_sampah":50,"t_total":100},{"id_device":2,"t_sampah":50,"t_total":100}]
data = json.loads(data)
rdd.parallelize(data)

#Operasi
def persen(data):
    operasi = (data['t_sampah']/data['t_total'])*100
    arr = {"persentase":operasi}
    data.append(arr)
    return data

rddBaru = rdd.map(persen)

datahasil = rddBaru.collect()
print(datahasil)

#status = proxy.updateDb(datahasil)
#print(status)
#proxy.cekData()