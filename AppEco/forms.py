from django import forms

sexos = [
    ('M', 'masculino'),
    ('F', 'femenino'),
    ('NB', 'no binario')
]

class PacienteFormulario(forms.Form):
    
    DNI= forms.IntegerField()
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    mail=forms.EmailField()
    fecha_nacimiento=forms.DateField()
    sexo=forms.CharField(max_length=2, choices=sexos, default='F')