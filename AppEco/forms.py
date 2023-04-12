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

class FormNuevaEcografia(forms.Form):
    fecha_estudio=forms.DateField()
    medico=forms.ForeignKey(Medico, null=True, blank=True, on_delete=models.SET_NULL)
    paciente=forms.ForeignKey(Paciente, on_delete=models.CASCADE)
    DBP=forms.FloatField()
    CC=forms.FloatField()
    CA=forms.FloatField()
    LF=forms.FloatField()
    PFE=forms.IntegerField()    