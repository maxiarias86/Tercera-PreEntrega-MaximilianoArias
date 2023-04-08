from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia

# Create your views here.

def inicio(request):
    return HttpResponse('vista inicio')
def pacientes(request):
    return HttpResponse('vista pacientes')
def medicos(request):
    return HttpResponse('vista medicos')
def ecografias(request):
    return HttpResponse('vista ecografias')