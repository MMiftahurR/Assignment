#!/usr/bin/python3 
 
import http.client 
 
def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    response = conn.getresponse()
    return response.getheaders(), response.read() 
 
for data in get("filkom.ub.ac.id", "/"):
    print(data)
    
print("\n spasi \n")
 
for data in get("filkom.ub.ac.id", "/auth"):
    print(data)