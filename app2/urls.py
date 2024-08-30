from django.urls import path
from app2.views import *
app_name='ootyhills'
urlpatterns=[
 path('ooty/',ooty,name='ooty')   
]