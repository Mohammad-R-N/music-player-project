from django.shortcuts import render



def home(request):
    return render('home/home.html')