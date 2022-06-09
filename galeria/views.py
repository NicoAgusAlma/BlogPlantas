from django.shortcuts import render
from django.views.generic import ListView
from plantas.models import Planta

# Create your views here.
class Galeria(ListView):
    model = Planta
    template_name = 'galeria/galeria.html'