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

def signpaciente(request):
    return render(request, 'med_app/signup-paciente.html')

def signprofissional(request):
    return render(request, 'med_app/signup-profissional.html')

def signin(request):
    return render(request, 'med_app/signin.html')

def obrigado(request):
    return render(request, 'med_app/obrigado.html')

def agendar(request):
    return render(request, 'med_app/agendar.html')