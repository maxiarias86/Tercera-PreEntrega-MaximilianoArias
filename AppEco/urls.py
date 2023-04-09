from django.urls import path
from AppEco.views import *

urlpatterns = [
    
    path("", inicio, name="inicioAppEco"),
    path("pacientes/", pacientes, name="pacientes"),
    path("medicos/", medicos, name="medicos"),
    path("ecografias/", ecografias, name="ecografias"),
    
]