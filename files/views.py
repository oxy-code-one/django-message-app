from django.shortcuts import render,HttpResponse
from django.templatetags.static import static
import os
# Create your views here.
def file_view(request,*args,**kwargs):
    pass

def upload_file(request,*args,**kwargs):
    if request.method == 'POST':
        print(request.FILES.keys())
        print(request.FILES["file"])
        handle_uploaded_file(request.FILES["file"])
        return HttpResponse("File uploaded")
    else:
        return HttpResponse("choose a file")
def download_file(request,*args,**kwargs):
    upload_dir = os.path.join(os.getcwd(),"static","upload")
    fileList = os.listdir( upload_dir )
    print( fileList )
    return HttpResponse(str(fileList))
def delete_file(request,*args,**kwargs):
    upload_dir = os.path.join(os.getcwd(),"static","upload")
    file = request.GET.get("file")
    file = os.path.join(upload_dir,file)
    response =""
    if file:
        if os.path.exists(file):
            os.remove(file)
            response = "file deleted"
        else:
            response = "file not found" 
    else:
        response = "invalid request"
    return HttpResponse(response)
def handle_uploaded_file(f):
    with open('static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)