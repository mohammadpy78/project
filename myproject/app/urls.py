from django.urls import path
from app.views import *

app_name='home'

urlpatterns=[
    path('',home)
]