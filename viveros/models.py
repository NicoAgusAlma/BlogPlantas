from django.db import models
from email.mime import image
from os import urandom
from django.contrib.auth.models import User

# Create your models here.
class Vivero(models.Model):
    nombre=models.CharField(max_length=40)
    provincia=models.CharField(max_length=40)
    imagen=models.ImageField(upload_to='imagenesViveros', null=True, blank=True)
    localidad=models.CharField(max_length=40)
    calle=models.CharField(max_length=40)
    altura=models.CharField(max_length=40)
    telefono=models.IntegerField()
    stockPlantas=models.CharField(max_length=2000)
    stockProductos=models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.nombre} en {self.localidad}'