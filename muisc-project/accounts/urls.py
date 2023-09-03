from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('otp/', otp, name='otp'),
    path('login/',login,name="login")]