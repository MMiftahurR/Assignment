# Import library xmlrpc
import xmlrpc.server

# Inisiasi server
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

# Definisi procedure atau fungsi
def penjumlahan(a,b):
    return (a+b)

# register fungsinya
server.register_function(penjumlahan, "penjumlahan")

# Running server RPC
server.serve_forever()