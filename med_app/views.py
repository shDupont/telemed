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


from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.shortcuts import render, redirect


def signup_paciente(request):
    # return render(request, 'med_app/signup-paciente.html')

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            ##login(request, user)
            # return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'med_app/signup-paciente.html', {'form': form})

def signprofissional(request):
    return render(request, 'med_app/signup-profissional.html')

def signin(request):
    return render(request, 'med_app/signin.html')

def obrigado(request):
    return render(request, 'med_app/obrigado.html')

def agendar(request):
    return render(request, 'med_app/agendar.html')

def logadoagendar(request):
    return render(request, 'med_app/logado-agendar.html')

def navlogado(request):
    return render(request, 'med_app/nav-logado.html')

def logadoconsulta(request):
    return render(request, 'med_app/logado-consulta.html')

def agendarconfirmar(request):
    return render(request, 'med_app/agendar-confirmar.html')

def posagendamento(request):
    return render(request, 'med_app/logado-com-consulta.html')

def posconsulta(request):
    return render(request, 'med_app/logado-com-historico.html')

def prechamada(request):
    return render(request, 'med_app/pre-chamada.html')

def avaliacao(request):
    return render(request, 'med_app/avaliacao.html')

def chamada(request):
    return render(request, 'med_app/chamada.html')

def configpaciente(request):
    return render(request, 'med_app/config-paciente.html')