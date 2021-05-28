from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('signup-paciente/', views.signpaciente),
    path('signup-profissional/', views.signprofissional),
    path('obrigado/', views.obrigado),
    path('agendar/', views.agendar),
    path('signin/', views.signin),
    path('login/', views.login),
    path('aboutus/', views.aboutus),
    path('logado-agendar', views.logadoagendar),
    path('nav-logado', views.navlogado),
    path('logado-consulta', views.logadoconsulta),
    path('agendar-confirmar', views.agendarconfirmar),
]