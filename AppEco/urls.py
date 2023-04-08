from django.urls import path
from AppEco.views import *

urlpatterns = [
    
    path("", inicio),
    path("pacientes/", pacientes),
    path("medicos/", medicos),
    path("ecografias/", ecografias),
    
]