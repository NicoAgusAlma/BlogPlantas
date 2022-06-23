from django.shortcuts import render
from plantas.forms import PlantaCustom
from plantas.models import Planta
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import random
import string

from problemas.models import Problema

# Create your views here.
# PLANTAS

def ui(request):
    return render (request, 'plantas/ui.html')

class PlantListView(ListView):
    model = Planta
    template_name = 'plantas/plantas_list.html'
    

class PlantDetailView(DetailView):
    model = Planta
    template_name = 'plantas/planta_detalle.html' 
   

class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')  
    form_class=PlantaCustom  
    def get_template_names(self):         
        return 'plantas/planta_form.html'

    # aqui la parte de testing sobre distintos campos:   
    # estos campos deben ser deshabilitados en forms.py para ser testeados.
    # una vez hecho el testeo, volver a habilitarlos 
    
    # def form_valid(self, form):
    #     str_len=20
    #     num_len=5
    #     nombrerandom =''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(str_len))
    #     nombreCrandom =''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(str_len))
    #     familiarandom =''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(str_len))
    #     sustratorandom =''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(str_len))
    #     preciorandom =''.join(random.choice(string.digits) for _ in range(num_len))
    #     frecuenciarandom =''.join(random.choice(string.digits) for _ in range(num_len))

    #     form.instance.nombreComun = nombrerandom 
    #     form.instance.nombreCientifico = nombreCrandom 
    #     form.instance.familia = familiarandom 
    #     form.instance.sustrato = sustratorandom 
    #     form.instance.precio = preciorandom 
    #     form.instance.frecuenciaRiego = frecuenciarandom 

    #     return super(PlantCreateView, self).form_valid(form)
    

class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')
    form_class=PlantaCustom  
    def get_template_names(self):         
        return 'plantas/planta_form.html'

class PlantDeleteView(LoginRequiredMixin, DeleteView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')
    def get_template_names(self):         
        return 'plantas/planta_confirm_delete.html'

