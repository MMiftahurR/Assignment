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
    if(len(sys.argv) >= 2):
        author = sys.argv[1]
        for i in range (2,len(sys.argv)):
            author = author+" ,"+sys.argv[i]
        urlAuthor = author.replace(" ", "%20")
        urlAuthor = urlAuthor.replace(",","")
        data = get("www.googleapis.com", "/books/v1/volumes?q=inauthor:"+urlAuthor)
        print("\nPengarang\t:",author)
        if(data["totalItems"] != 0):
            print("Judul\t\t:")
            maks =  data["totalItems"]
            if (maks > 10):
                maks = 10
            for i in range (0,maks):
                print("- ",data["items"][i]["volumeInfo"].get("title"))
        else:
            print("Judul\t: None",)
    else:
        print("Format(Windows): py [filename] [author]")
        print("Format(Ubuntu): ./[filename] [author] ")
        
if __name__ == "__main__":
    main()