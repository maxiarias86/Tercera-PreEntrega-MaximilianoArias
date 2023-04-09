from django.db import models

# Create your models here.

sexos = [
    ('M', 'masculino'),
    ('F', 'femenino'),
    ('NB', 'no binario')
]

class Paciente(models.Model):
    DNI= models.IntegerField()
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    mail=models.EmailField()
    fecha_nacimiento=models.DateField()
    sexo=models.CharField(max_length=2, choices=sexos, default='F')
    
    def __str__(self):
        return f'Paciente {self.nombre} {self.apellido}, DNI {self.DNI}'

class Medico(models.Model):
    MN= models.IntegerField()
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    mail=models.EmailField()

    def __str__(self):
        return f'Dr. {self.apellido}, {self.nombre}, MN: {self.MN}'

class Ecografia(models.Model):
    fecha_estudio=models.DateField()
    medico=models.ForeignKey(Medico, null=True, blank=True, on_delete=models.SET_NULL)
    paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE)
    DBP=models.FloatField()
    CC=models.FloatField()
    CA=models.FloatField()
    LF=models.FloatField()
    PFE=models.IntegerField()