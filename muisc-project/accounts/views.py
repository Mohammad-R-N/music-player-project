from django.shortcuts import render



def home(request):
    return render(request,'accounts/home/home.html')

def otp(request):
    return render(request,'accounts/login/otp.html')