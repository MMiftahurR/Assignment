# Import library xmlrpc
import xmlrpc.client

# Inisiasi proxy ke server
proxy = xmlrpc.client.ServerProxy("http://localhost:7778/")

hasil = proxy.penjumlahan(20,10)

print(hasil)