import datetime
import time
from django.shortcuts import render,HttpResponse
from .models import Sense,Sensor

# Create your views here.
def add_data(request,*args,**kwargs):
    response = HttpResponse()
    if(request.GET.get("id") and request.GET.get("value") and request.GET.get("min") and len(request.GET.get("value"))==6 and len(request.GET.get("min"))==2):
        # Sense.objects.create(userID= int(request.GET.get("id")) , activity=request.GET.get("value"))
        curtime = str(datetime.datetime.today())[:13]
        curtime = curtime.replace(" ","-")
        senseObject , created = Sensor.objects.get_or_create(userID = int(request.GET.get("id")), time = curtime)
        update_sensor(senseObject,request.GET.get("min"),request.GET.get("value"))
        print(senseObject.userID , created, curtime)
        response.content = "saved succesfully"
    else:
        response.content = "Bad Request"
        response.status_code = 400
    return response


def get_data(request,*args,**kwargs):
    startCall = time.time()
    response = HttpResponse()
    timerecv = request.GET.get("time")
    userID = int(request.GET.get("user"))
    if(time and userID):
        senseData = Sensor.objects.get(time=timerecv,userID= userID)
        senseArray = []
        for a in range(0,60):
            senseArray.append(getattr(senseData,"activity"+str(a)))
        response.content = str(senseArray)
    else:
        response.content = "Bad Request"
        response.status_code = 400
    timeTaken = time.time()-startCall
    print("processing time -> ",str(timeTaken))
    return response

def update_sensor(model,min,value):
    if(min=="01"):
         model.activity1=value
         model.save(update_fields=['activity1'])
    elif(min=="02"):
         model.activity2=value
         model.save(update_fields=['activity2'])
    elif(min=="03"):
         model.activity3=value
         model.save(update_fields=['activity3'])
    elif(min=="04"):
         model.activity4=value
         model.save(update_fields=['activity4'])
    elif(min=="05"):
         model.activity5=value
         model.save(update_fields=['activity5'])
    elif(min=="06"):
         model.activity6=value
         model.save(update_fields=['activity6'])
    elif(min=="07"):
         model.activity7=value
         model.save(update_fields=['activity7'])
    elif(min=="08"):
         model.activity8=value
         model.save(update_fields=['activity8'])
    elif(min=="09"):
         model.activity9=value
         model.save(update_fields=['activity9'])
    elif(min=="10"):
         model.activity10=value
         model.save(update_fields=['activity10'])
    elif(min=="11"):
         model.activity11=value
         model.save(update_fields=['activity11'])
    elif(min=="12"):
         model.activity12=value
         model.save(update_fields=['activity12'])
    elif(min=="13"):
         model.activity13=value
         model.save(update_fields=['activity13'])
    elif(min=="14"):
         model.activity14=value
         model.save(update_fields=['activity14'])
    elif(min=="15"):
         model.activity15=value
         model.save(update_fields=['activity15'])
    elif(min=="16"):
         model.activity16=value
         model.save(update_fields=['activity16'])
    elif(min=="17"):
         model.activity17=value
         model.save(update_fields=['activity17'])
    elif(min=="18"):
         model.activity18=value
         model.save(update_fields=['activity18'])
    elif(min=="19"):
         model.activity19=value
         model.save(update_fields=['activity19'])
    elif(min=="20"):
         model.activity20=value
         model.save(update_fields=['activity20'])
    elif(min=="21"):
         model.activity21=value
         model.save(update_fields=['activity21'])
    elif(min=="22"):
         model.activity22=value
         model.save(update_fields=['activity22'])
    elif(min=="23"):
         model.activity23=value
         model.save(update_fields=['activity23'])
    elif(min=="24"):
         model.activity24=value
         model.save(update_fields=['activity24'])
    elif(min=="25"):
         model.activity25=value
         model.save(update_fields=['activity25'])
    elif(min=="26"):
         model.activity26=value
         model.save(update_fields=['activity26'])
    elif(min=="27"):
         model.activity27=value
         model.save(update_fields=['activity27'])
    elif(min=="28"):
         model.activity28=value
         model.save(update_fields=['activity28'])
    elif(min=="29"):
         model.activity29=value
         model.save(update_fields=['activity29'])
    elif(min=="30"):
         model.activity30=value
         model.save(update_fields=['activity30'])
    elif(min=="31"):
         model.activity31=value
         model.save(update_fields=['activity31'])
    elif(min=="32"):
         model.activity32=value
         model.save(update_fields=['activity32'])
    elif(min=="33"):
         model.activity33=value
         model.save(update_fields=['activity33'])
    elif(min=="34"):
         model.activity34=value
         model.save(update_fields=['activity34'])
    elif(min=="35"):
         model.activity35=value
         model.save(update_fields=['activity35'])
    elif(min=="36"):
         model.activity36=value
         model.save(update_fields=['activity36'])
    elif(min=="37"):
         model.activity37=value
         model.save(update_fields=['activity37'])
    elif(min=="38"):
         model.activity38=value
         model.save(update_fields=['activity38'])
    elif(min=="39"):
         model.activity39=value
         model.save(update_fields=['activity39'])
    elif(min=="40"):
         model.activity40=value
         model.save(update_fields=['activity40'])
    elif(min=="41"):
         model.activity41=value
         model.save(update_fields=['activity41'])
    elif(min=="42"):
         model.activity42=value
         model.save(update_fields=['activity42'])
    elif(min=="43"):
         model.activity43=value
         model.save(update_fields=['activity43'])
    elif(min=="44"):
         model.activity44=value
         model.save(update_fields=['activity44'])
    elif(min=="45"):
         model.activity45=value
         model.save(update_fields=['activity45'])
    elif(min=="46"):
         model.activity46=value
         model.save(update_fields=['activity46'])
    elif(min=="47"):
         model.activity47=value
         model.save(update_fields=['activity47'])
    elif(min=="48"):
         model.activity48=value
         model.save(update_fields=['activity48'])
    elif(min=="49"):
         model.activity49=value
         model.save(update_fields=['activity49'])
    elif(min=="50"):
         model.activity50=value
         model.save(update_fields=['activity50'])
    elif(min=="51"):
         model.activity51=value
         model.save(update_fields=['activity51'])
    elif(min=="52"):
         model.activity52=value
         model.save(update_fields=['activity52'])
    elif(min=="53"):
         model.activity53=value
         model.save(update_fields=['activity53'])
    elif(min=="54"):
         model.activity54=value
         model.save(update_fields=['activity54'])
    elif(min=="55"):
         model.activity55=value
         model.save(update_fields=['activity55'])
    elif(min=="56"):
         model.activity56=value
         model.save(update_fields=['activity56'])
    elif(min=="57"):
         model.activity57=value
         model.save(update_fields=['activity57'])
    elif(min=="58"):
         model.activity58=value
         model.save(update_fields=['activity58'])
    elif(min=="59"):
         model.activity59=value
         model.save(update_fields=['activity59'])
    elif(min=="00"):
         model.activity0=value
         model.save(update_fields=['activity0'])


#>>> s = Sense.objects.filter(timestamp__time__range=(datetime.time(9,32,0),datetime.time(9,33,1))