from django.urls import path
from app1.views import *
app_name='foodie'
urlpatterns=[
 path('biriyani/',biriyani,name='biriyani')   
]