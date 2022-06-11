from django.db import models
from django.contrib.auth.models import User
from viveros.models import Vivero

# Create your models here.
class Producto(models.Model):
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField(help_text='Precio en U$s blue.')
    imagen=models.ImageField(upload_to='imagenesProductos', null=True, blank=True)
    solucionaProblemas=models.CharField(help_text='Problemas que soluciona.', max_length=200)
    puntoDeVenta=models.ForeignKey(Vivero, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombre}'