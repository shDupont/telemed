from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('signup-paciente/', views.signpaciente, name='signpaciente'),
    path('signup-profissional/', views.signprofissional, name='signprofissional'),
    path('obrigado/', views.obrigado),
    path('agendar/', views.agendar),
    path('signin/', views.signin, name='signin'),
    path('login/', views.login),
    path('aboutus/', views.aboutus),
    path('logado-agendar', views.logadoagendar),
    path('nav-logado', views.navlogado),
    path('logado-consulta', views.logadoconsulta),
    path('agendar-confirmar', views.agendarconfirmar),
    path('pos-agendamento', views.posagendamento),
    path('pos-consulta', views.posconsulta),
    path('pre-chamada', views.prechamada),
    path('avaliacao', views.avaliacao),
    path('chamada', views.chamada),
    path('config-paciente', views.configpaciente),
]