from cProfile import label
from email.mime import image
from os import urandom
from django.db import models
from viveros.models import Vivero
from problemas.models import Problema

# Create your models here.

class Planta(models.Model):
    nombreComun=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)
    familia=models.CharField(help_text='<br> Arbol, planta, flor, cactacea, etc.', max_length=50)
    sustrato=models.CharField(help_text='<br> Algun tipo de tierra especial?', max_length=50)
    precio=models.IntegerField(help_text='<br> Precio en U$s blue.')
    viveros=models.ManyToManyField(Vivero, blank=True, help_text='<br> Mantenga CTRL para seleccionar varios')
    peligrosComunes=models.ManyToManyField(Problema, blank=True, help_text='<br> Mantenga CTRL para seleccionar varios')
    interior=models.BooleanField(default=True, verbose_name='Es planta de interior?')
    luzDirecta=models.BooleanField(default=False, verbose_name='Luz solar directa?')
    frecuenciaRiego=models.IntegerField(help_text='<br> Riegos mensuales.')
    descripcion=models.TextField(help_text='<br> Descripcion de la planta.', max_length=3000)
    
    def __str__(self):
        return f'{self.nombreComun} / {self.nombreCientifico}'

class ImagenPlanta(models.Model):
    planta=models.ForeignKey(Planta , on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)
    def __str__(self):
        return f"{self.imagen.url}"