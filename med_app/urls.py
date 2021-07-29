from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('signup-paciente/', views.signup_paciente, name='signup_paciente'),
    path('signup-profissional/', views.signprofissional, name='signprofissional'),
    path('obrigado/', views.obrigado, name='obrigado'),
    path('agendar/', views.agendar, name='agendar'),
    path('signin/', views.signin, name='signin'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('logado-agendar', views.logadoagendar, name='agendar'),
    path('nav-logado', views.navlogado, name='nav-logado'),
    path('logado-consulta', views.logadoconsulta, name='logado-consulta'),
    path('agendar-confirmar', views.agendarconfirmar, name='agendar-confirmacao'),
    path('pos-agendamento', views.posagendamento, name='consultas'),
    path('pos-consulta', views.posconsulta, name='historico'),
    path('pre-chamada', views.prechamada, name='pre-chamada'),
    path('avaliacao', views.avaliacao, name='avaliacao'),
    path('chamada', views.chamada, name='chamada'),
    path('config-paciente', views.configpaciente, name='config-paciente'),
]