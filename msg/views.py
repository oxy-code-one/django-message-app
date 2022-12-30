import datetime
import json
import time
from django.shortcuts import render,HttpResponse
from .models import Sense
# Create your views here.
def add_data(request,*args,**kwargs):
    response = HttpResponse()
    if(request.GET.get("id") and request.GET.get("value") and len(request.GET.get("value"))==6):
        Sense.objects.create(userID= int(request.GET.get("id")) , activity=request.GET.get("value"))
        response.content = "saved succesfully"
    else:
        response.content = "Bad Request"
        response.status_code = 400
    return response

def get_data(request,*args,**kwargs):
    startCall = time.time()
    print("called")
    response = HttpResponse()
    startTime = request.GET.get("start")
    endTime = request.GET.get("end")
    if(startTime and endTime ):
        stime = startTime.split(",") 
        etime = endTime.split(",")
        senseData = Sense.objects.filter(timestamp__time__range=(datetime.time(int(stime[0]),int(stime[1]),int(stime[2])),datetime.time(int(etime[0]),int(etime[1]),int(etime[2]))))
        print("database fetch->",time.time()-startCall)#,senseData[0].activity
        senseArray = []
        for data in senseData:
            senseArray.append(data.activity)         
        # senseArray[]=senseData.count()
        response.content = "got data"#str(senseArray)
    else:
        response.content = "Bad Request"
        response.status_code = 400
    timeTaken = time.time()-startCall
    print("processing time -> ",str(timeTaken))
    return response

#>>> s = Sense.objects.filter(timestamp__time__range=(datetime.time(9,32,0),datetime.time(9,33,1))