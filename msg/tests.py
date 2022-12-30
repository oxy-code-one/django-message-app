from django.test import TestCase
# Create your tests here.
import requests
import time 
import sys

start_time = time.time()
req_count = 1000000

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def req(count):
    if(count<0):
        return False
    url = "http://127.0.0.1:8000/sensor/api/add?id=1&value=000001"
    x = requests.get(url)
    if(x.status_code==200):
        print_there(5,5,x.text+" "+str(count))
        return True
    else:
        print("failed",x.text,str(x.status_code))

while(req(req_count)):
    req_count-=1
print("seconds taken ",str(time.time()-start_time))