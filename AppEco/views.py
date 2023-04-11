from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia
from AppEco.forms import PacienteFormulario

# Create your views here.

def inicio(request):
    return render (request, 'AppEco/inicio.html')

def pacientes(request):
    return render (request, 'AppEco/pacientes.html')

def medicos(request):
    return render (request, 'AppEco/medicos.html')

def ecografias(request):
    return render (request, 'AppEco/ecografias.html')

def pacienteFormulario(request):
    if request.method=="POST":
        miFormulario = PacienteFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
        
            DNI= informacion['DNI']
            nombre= informacion['nombre']
            apellido= informacion['apellido']
            mail= informacion['mail']
            fecha_nacimiento= informacion['fecha_nacimiento']
            sexo= informacion['sexo']

            paciente=Paciente(DNI=DNI, nombre=nombre, apellido=apellido, mail=mail, fecha_nacimiento=fecha_nacimiento,sexo=sexo)
            paciente.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        miFormulario=PacienteFormulario()
        return render(request, "AppEco/pacienteFormulario.html",{"miFormulario":miFormulario})
    
def busquedaPaciente(request):
    return render(request, "AppEco/busquedaPaciente.html")

def buscar(request):
    DNI=request.GET["DNI"]
    if DNI!="":
        pacientes=Paciente.objects.filter(DNI__icontains=DNI)
        return render(request, "AppEco/resultadosBusqueda.html", {"pacientes": pacientes})
    else:
        return render(request, "AppEco/busquedaPaciente.html", {"mensaje": "Ingrese el DNI del paciente a buscar"})