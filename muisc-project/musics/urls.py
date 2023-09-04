from django.urls import path
from .views import *

urlpatterns=[
    path('playlist-detail/',playlist_detail,name='playlist-detail'),
    ]