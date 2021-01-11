import time
from datetime import datetime


import os

import parser
import json
from bs4 import BeautifulSoup
import requests

##-----Functions-----## 
#Write Files
def write(fname, data):
    print("Making File")
    with open(f"{fname}", "w") as f:
        f.write(data)
    print("Done Writing")

def append(fname, data):
    print("Adding Data")
    with open(f"{fname}", "a") as f:
        f.write(data)
    print("Done Adding")

##-----Main Code Segment-----##
def main():
    print("--- Starting ---")
    start_time = time.time()

    #NOTE: Websites check for automation, add header to avoid issues
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
    cookie = dict(cookies_are='working')

    link = "https://www.amazon.com/Razer-Blade-Gaming-Laptop-Thunderbolt/dp/B088ZW8KKC/ref=sr_1_4?dchild=1&keywords=razer+laptop&qid=1610254319&s=pc&sr=1-4"
    req = requests.get( link, headers = header, cookies = cookie)
    print(req)
    print(req.text)

    soup = BeautifulSoup(req.text,'lxml')
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #price = soup.find(id="price_inside_buybox").get_text().strip().strip('$')
    #print(price)
    
    #append("tracking.txt", f"{now}\t{price}\n")
    write("test.html", soup.prettify())

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()