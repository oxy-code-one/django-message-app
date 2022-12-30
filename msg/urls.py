from django.urls import path 
from .views import add_data,get_data
urlpatterns = [
    path("api/add",add_data),
    path("api/get",get_data),
]