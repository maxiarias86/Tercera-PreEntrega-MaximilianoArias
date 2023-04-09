from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia

# Create your views here.

def inicio(request):
    return render (request, 'inicio.html')
def pacientes(request):
    return render (request, 'pacientes.html')
def medicos(request):
    return render (request, 'medicos.html')
def ecografias(request):
    return render (request, 'ecografias.html')