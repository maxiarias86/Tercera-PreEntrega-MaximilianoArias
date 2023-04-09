from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia

# Create your views here.

def inicio(request):
    return render (request, 'AppEco/inicio.html')
def pacientes(request):
    return render (request, 'AppEco/pacientes.html')
def medicos(request):
    return render (request, 'AppEco/medicos.html')
def ecografias(request):
    return render (request, 'AppEco/ecografias.html')