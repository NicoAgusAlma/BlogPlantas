from django.shortcuts import render
from django.views.generic import ListView
from plantas.models import Planta
from blog.models import Posteo

# Create your views here.
class Galeria(ListView):
    model = Planta
    posteos = Posteo.objects.all()
    extra_context = {'posteos':posteos}
    template_name = 'galeria/galeria.html'