from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'med_app/index.html')

def signup(request):
    return render(request, 'med_app/signup.html')

def login(request):
    return render(request, 'med_app/login.html')

def aboutus(request):
    return render(request, 'med_app/aboutus.html')