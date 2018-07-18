#!/usr/bin/python3
import httplib2
import json
import sys
def get(domain, path):
    url = "https://" + domain + path
    h = httplib2.Http(".cache")
    resp, cont = h.request(url,"GET")
    return json.loads(cont)

def main():
    if(len(sys.argv) == 2):
        isbn = sys.argv[1]
        data = get("www.googleapis.com", "/books/v1/volumes?q="+isbn+"+isbn")
        print("\nJudul\t\t: ", end='')
        print(data["items"][0]["volumeInfo"].get("title"))
        if(data["items"][0]["volumeInfo"].get("authors")):
            print("Pengarang\t:")
            for author in data["items"][0]["volumeInfo"].get("authors"):
                print("- "+author)
        print("Penerbit\t: ", end='')
        print(data["items"][0]["volumeInfo"].get("publisher"))
        print("Tanggal Terbit\t: ", end='')
        print(data["items"][0]["volumeInfo"].get("publishedDate"))
    else:
        print("Format(Windows): py [filename] [isbn]")
        print("Format(Ubuntu): ./[filename] [isbn] ")

if __name__ == "__main__":
    main()