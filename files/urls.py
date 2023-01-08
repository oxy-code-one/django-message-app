from django.urls import path 
from .views import upload_file,download_file,file_view,delete_file
urlpatterns = [
    path("",file_view),
    path("add",upload_file),
    path("get",download_file),
    path("del",delete_file),
]