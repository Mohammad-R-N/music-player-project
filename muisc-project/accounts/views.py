from django.shortcuts import render
from django.views import View

app_name="accounts"
def home(request):
    return render(request,'accounts/home/home.html')

app_name="accounts"
def otp(request):
    return render(request,'accounts/login/otp.html')

app_name="accounts"
def login(request):
    return render(request,'accounts/login/login.html')


app_name="accounts"
class UserSignUp(View):

    def get(self,request):
        
        return render(request,"accounts/signup/signup.html")

    def post(self,request):
        pass

app_name="accounts"
def profile(request):
    return render(request,'accounts/profile/profile.html')

app_name="accounts"
def myplaylists(request):
    return render(request,'accounts/myplaylists/myplaylists.html')
