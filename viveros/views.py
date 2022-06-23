
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from viveros.models import Vivero
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# VIVEROS

class GreenHouseListView(ListView):
    model = Vivero
    template_name = 'viveros/viveros_list.html'

class GreenHouseDetailView(DetailView):
    model = Vivero
    template_name = 'viveros/vivero_detalle.html'

class GreenHouseCreateView(LoginRequiredMixin, CreateView):
    model = Vivero
    success_url = reverse_lazy('viveros:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono', 'imagen']
    def get_template_names(self):         
        return 'viveros/vivero_form.html'

class GreenHouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Vivero
    success_url = reverse_lazy('viveros:ListaViveros')
    fields = ['nombre','provincia','localidad','calle','altura','telefono', 'imagen']
    def get_template_names(self):         
        return 'viveros/vivero_form.html'

class GreenHouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Vivero
    success_url = reverse_lazy('viveros:ListaViveros')
    def get_template_names(self):         
        return 'viveros/vivero_confirm_delete.html'