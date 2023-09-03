from django.shortcuts import render



def home(request):
    return render(request,'accounts/home/home.html')

def otp(request):
    return render(request,'accounts/login/otp.html')

def login(request):
    return render(request,'accounts/login/login.html')

def signup(request):
    return render(request,'accounts/signup/signup.html')