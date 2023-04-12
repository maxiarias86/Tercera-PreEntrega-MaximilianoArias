from django import forms

generos = [
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
    sexo=forms.ChoiceField(choices=generos, required=True, label='Seleccione su genero')