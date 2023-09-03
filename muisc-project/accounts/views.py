from django.shortcuts import render



def home(request):
    return render(request,'accounts/home/home.html')

def otp(request):
    return render(request,'accounts/login/otp.html')

def login(request):
    return render(request,'accounts/login/login.html')

def signin(request):
    return render(request,'accounts/signin/signin.html')