import http.client
import json
import sys
def get(domain, url):
    conn = http.client.HTTPSConnection(domain)
    conn.request("GET", url)
    resp = conn.getresponse()
    payload = resp.read()
    return json.loads(payload)

def main():
    if(len(sys.argv) == 2):
        isbn = sys.argv[1]
        jsonData = get("www.googleapis.com", "/books/v1/volumes?q="+isbn+"+isbn")
        #1. 9788170084266
        #2. 9780761825616 //2 authors
        #3. 9781603092739 //no publisher
        #4. 9781435723863 //no author + publishedDate
        print("\nJudul\t: ", end='')
        print(jsonData["items"][0]["volumeInfo"].get("title"))
        if(jsonData["items"][0]["volumeInfo"].get("authors")):
            print("Pengarang\t:")
            for author in jsonData["items"][0]["volumeInfo"].get("authors"):
                print("- "+author)
        else:
            print("Pengarang\t: ", end='')
            print(jsonData["items"][0]["volumeInfo"].get("authors"))
        print("Penerbit\t: ", end='')
        print(jsonData["items"][0]["volumeInfo"].get("publisher"))
        print("Tanggal Terbit\t: ", end='')
        print(jsonData["items"][0]["volumeInfo"].get("publishedDate"))
    else:
        print("\nFormat: python3 [filename] [isbn]")

if __name__ == "__main__":
    main()