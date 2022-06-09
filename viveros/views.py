from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from viveros.models import Vivero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# VIVEROS

class ViveroList(ListView):
    model = Vivero
    template_name = 'viveros/viveros_list.html'

class ViveroDetail(DetailView):
    model = Vivero
    template_name = 'viveros/vivero_detalle.html'

class ViveroCreate(LoginRequiredMixin, CreateView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono','stockPlantas','stockProductos', 'imagen']
    def get_template_names(self):         
        return 'viveros/vivero_form.html'

class ViveroUpdate(LoginRequiredMixin, UpdateView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono','stockPlantas','stockProductos', 'imagen']
    def get_template_names(self):         
        return 'viveros/vivero_form.html'

class ViveroDelete(LoginRequiredMixin, DeleteView):
    model = Vivero
    success_url = reverse_lazy('BlogPlantas:ListaViveros')
    def get_template_names(self):         
        return 'viveros/vivero_confirm_delete.html'