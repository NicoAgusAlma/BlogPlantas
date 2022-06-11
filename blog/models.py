from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.
class Posteo(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField(auto_now_add=True)
    texto=RichTextField(blank=True, null=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenesPosteos', null=True, blank=True)
    categoria=models.CharField(max_length=100, default='')
    

    def __str__(self):
        return f'{self.titulo} / {self.fecha} / {self.autor}'

class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'
