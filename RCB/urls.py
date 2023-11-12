from django.urls import path
from RCB.views import *

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('siraj/',siraj,name='siraj'),
]