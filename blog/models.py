from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posteo(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    fecha=models.DateField(help_text='AAAA/MM/DD')
    texto=models.TextField(max_length=5000)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='imagenesPosteos', null=True, blank=True)
    categoria=models.CharField(max_length=100, default='')
    tags=models.CharField(max_length=100, default='')


    def __str__(self):
        return f'{self.titulo} / {self.fecha} / {self.autor}'
