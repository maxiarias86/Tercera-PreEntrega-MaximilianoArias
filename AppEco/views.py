from django.shortcuts import render
from django.http import HttpResponse
from AppEco.models import Paciente, Medico, Ecografia
from AppEco.forms import PacienteFormulario, FormNuevaEcografia, MedicoFormulario

# Create your views here.

def inicio(request):
    return render (request, 'AppEco/inicio.html')

'''
def pacientes(request):
    return render (request, 'AppEco/pacientes.html')
'''

def pacientes(request):
    if request.method == "POST":
        form = PacienteFormulario(request.POST)
        if form.is_valid():
            paciente=Paciente()
            paciente.DNI= form.cleaned_data ['DNI']
            paciente.nombre=form.cleaned_data ['nombre']
            paciente.apellido=form.cleaned_data ['apellido']
            paciente.mail=form.cleaned_data ['mail']
            paciente.fecha_nacimiento=form.cleaned_data ['fecha_nacimiento']
            paciente.sexo=form.cleaned_data ['sexo']
            paciente.save()
            form=PacienteFormulario()
    else:
        form=PacienteFormulario()
        
    pacientes=Paciente.objects.all()

    return render (request, 'AppEco/pacientes.html', {'pacientes': pacientes, 'form':form})

def medicos(request):
    return render (request, 'AppEco/medicos.html')

def ecografias(request):
    return render (request, 'AppEco/ecografias.html')

def pacienteFormulario(request):
    if request.method == "POST":
        form = PacienteFormulario(request.POST)

        if form.is_valid:
            informacion = form.cleaned_data
        
            dni= informacion['DNI']
            nombre= informacion['nombre']
            apellido= informacion['apellido']
            mail= informacion['mail']
            fecha_nacimiento= informacion['fecha_nacimiento']
            sexo= informacion['sexo']

            paciente=Paciente(DNI=dni, nombre=nombre, apellido=apellido, mail=mail, fecha_nacimiento=fecha_nacimiento,sexo=sexo)
            paciente.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        form=PacienteFormulario()
        return render(request, "AppEco/pacienteFormulario.html",{"form":form})
    
def busquedaPaciente(request):
    return render(request, "AppEco/busquedaPaciente.html")
    
def buscar(request):
    try:
        DNI = request.GET["DNI"]
    except KeyError:
        return render(request, "AppEco/busquedaPaciente.html", {"mensaje": "Ingrese el DNI del paciente a buscar"})

    if DNI!="":
        pacientes = Paciente.objects.filter(DNI__icontains=DNI)
        if len(pacientes) == 0:
            mensaje = f"No se encontraron pacientes con DNI {DNI}"
            return render(request, "AppEco/resultadosBusqueda.html", {"mensaje": mensaje})
        else:
            return render(request, "AppEco/resultadosBusqueda.html", {"pacientes": pacientes})
    else:
        return render(request, "AppEco/busquedaPaciente.html", {"mensaje": "Ingrese el DNI del paciente a buscar"})
    
def nuevaEco(request):
    if request.method=="POST":
        miFormulario = FormNuevaEcografia(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
        
            fecha_estudio= informacion['fecha_estudio']
            medico=informacion['medico']
            paciente=informacion['paciente']
            DBP=informacion['DBP']
            CC=informacion['CC']
            CA=informacion['CA']
            LF=informacion['LF']
            PFE=informacion['PFE']

            ecografia=Ecografia(fecha_estudio=fecha_estudio, medico=medico, paciente=paciente, DBP=DBP, CC=CC, CA=CA, LF=LF, PFE=PFE)
            ecografia.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        miFormulario=FormNuevaEcografia()
        return render(request, "AppEco/ecografiaFormulario.html",{"miFormulario":miFormulario})
    
def medicoFormulario(request):
    if request.method == "POST":
        form = MedicoFormulario(request.POST)

        if form.is_valid:
            informacion = form.cleaned_data
        
            mn= informacion['MN']
            nombre= informacion['nombre']
            apellido= informacion['apellido']
            mail= informacion['mail']
            
            medico=Medico(MN=mn, nombre=nombre, apellido=apellido, mail=mail)
            medico.save()
            return render(request, "AppEco/inicio.html")
    
    else:
        form=MedicoFormulario()
        return render(request, "AppEco/medicoFormulario.html",{"form":form})