from django.shortcuts import render
from plantas.forms import PlantaCustom
from plantas.models import Planta
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from problemas.models import Problema

# Create your views here.
# PLANTAS

def ui(request):
    return render (request, 'plantas/ui.html')

class PlantaList(ListView):
    model = Planta
    template_name = 'plantas/plantas_list.html'
    

class PlantaDetail(DetailView):
    model = Planta
    template_name = 'plantas/planta_detalle.html' 
   

class PlantaCreate(LoginRequiredMixin, CreateView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')  
    form_class=PlantaCustom  
    # fields = ['nombreComun','nombreCientifico','familia','sustrato','precio','viveros','peligrosComunes','interior','luzDirecta','frecuenciaRiego','descripcion', 'imagen']
    def get_template_names(self):         
        return 'plantas/planta_form.html'

class PlantaUpdate(LoginRequiredMixin, UpdateView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')
    form_class=PlantaCustom  
    # fields = ['nombreComun','nombreCientifico','familia','sustrato','precio','viveros','peligrosComunes','interior','luzDirecta','frecuenciaRiego','descripcion']
    def get_template_names(self):         
        return 'plantas/planta_form.html'

class PlantaDelete(LoginRequiredMixin, DeleteView):
    model = Planta
    success_url = reverse_lazy('plantas:ListaPlantas')
    def get_template_names(self):         
        return 'plantas/planta_confirm_delete.html'

