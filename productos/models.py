from django.db import models
from django.contrib.auth.models import User
from viveros.models import Vivero

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField(help_text='Precio en U$s blue.')
    imagen=models.ImageField(upload_to='imagenesProductos', null=True, blank=True)
    puntoDeVenta=models.ManyToManyField(Vivero, blank=True, help_text='<br> Mantenga CTRL para seleccionar varios')

    def __str__(self):
        return f'{self.nombre}'