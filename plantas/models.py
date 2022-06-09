from email.mime import image
from os import urandom
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Planta(models.Model):
    nombreComun=models.CharField(max_length=40)
    nombreCientifico=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)
    familia=models.CharField(help_text='Arbol, planta, flor, cactacea, etc.', max_length=50)
    sustrato=models.CharField(help_text='Algun tipo de tierra especial?', max_length=50)
    precio=models.IntegerField(help_text='Precio en U$s blue.')
    viveros=models.CharField(help_text='Viveros donde encontrarla.', max_length=100)
    peligrosComunes=models.CharField(help_text='Problemas más usuales.', max_length=100)
    interior=models.BooleanField('interior', default=True)
    luzDirecta=models.BooleanField(default=False, help_text='Necesita luz solar directa?.')
    frecuenciaRiego=models.IntegerField(help_text='Riegos mensuales.')
    descripcion=models.CharField(help_text='Descripcion de la planta.', max_length=3000)
    
    def __str__(self):
        return f'{self.nombreComun} / {self.nombreCientifico}'

class ImagenPlanta(models.Model):
    planta=models.ForeignKey(Planta , on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenesPlantas', null=True, blank=True)
    def __str__(self):
        return f"{self.imagen.url}"