import time
import parser
import json
import requests

##-----Functions-----## 
#Write Files
def write(fname, data):
    print("Making File")
    with open(f"{fname}", "w") as f:
        f.write(data)
    print("Done Writing")
    
def writeJson(fname, data):
    print("Making File")
    with open(fname,'w') as out:
    	json.dump(data, out, indent = 4)
    print("Done")

def append(fname, data):
    print("Adding Data")
    with open(f"{fname}", "a") as f:
        f.write(data)
    print("Done Adding")

def saveImg(fname, data):
    print("Making Img")
    with open(fname,'wb') as out:
    	out.write(data)
    print("Done")    	

##-----Main Code Segment-----##
def main():
    print("--- Starting ---")
    start_time = time.time()

    #NOTE: Websites check for automation, add header to avoid issues
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
 
    base_url = "reddit.com"
    account = "r/wallpapers"
    mode ="new"
    options = ".json?count=25" #Figure out what these mean
    
    req = requests.get(f"https://{base_url}/{account}/{mode}.json?count=25", headers = header)
    print(req)
    #print(req.text)
    res = json.loads(req.text)
    writeJson("data.txt", res)
    print("--- %s seconds ---" % (time.time() - start_time))

def main_1():
    img_types = ( "jpg" , "png" )
    print("--- Starting ---"); start_time = time.time()

    #data = place input
    with open("data.txt", "r") as f:
    	data = json.load(f)
    print(len(data['data']['children']))
    
    #Find the url
    for post in data['data']['children']:
        check = post['data']['url']
        print(check)
        if check.endswith(img_types):
            fname = check.split("/")[-1]
            req = requests.get(check)
            print(req.content)
        #Prevent oversending requests
        time.sleep(30)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
    #main_1()
