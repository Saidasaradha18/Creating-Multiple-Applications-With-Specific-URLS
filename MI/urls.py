from django.urls import path
from MI.views import *

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
    path('bumrah/',bumrah,name='bumrah'),
]