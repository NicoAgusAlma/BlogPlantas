from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto

# Create your models here.
class Problema(models.Model):
    nombreProblema=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesProblemas', null=True, blank=True)
    peligro=models.CharField(max_length=10)
    productos=models.ManyToManyField(Producto, help_text='<br> Mantenga CTRL para seleccionar varios')
    solucion=models.TextField(help_text='<br>Manera de solucionarlo', max_length=2000)

    def __str__(self):
        return f'{self.nombreProblema}'
