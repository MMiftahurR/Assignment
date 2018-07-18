# Import library xmlrpc
import xmlrpc.client
import pyspark

# Inisiasi proxy ke server
proxy = xmlrpc.client.ServerProxy("http://[IP coba1.py]:7778/")

sc = SparkContext.getOrCreate()
data = proxy.getDataDevice()
rdd.parallelize(data)

#Operasi
def persen(data):
    operasi = (data['t_sampah']/data['t_total'])*100
    arr = {"persentase":operasi}
    data.append(arr)
    return data

datahasil = rddBaru_yang_telah_diproses

status = proxy.updateDb(datahasil)
print(status)
proxy.cekData()