from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Problema(models.Model):
    nombreProblema=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesProblemas', null=True, blank=True)
    peligro=models.CharField(help_text='Bajo, Medio o Alto', max_length=10)
    productos=models.CharField(help_text='Productos de ayuda.', max_length=50)
    solucion=models.CharField(help_text='Manera de solucionarlo', max_length=2000)

    def __str__(self):
        return f'{self.nombreProblema} / {self.nombreCientifico}'
