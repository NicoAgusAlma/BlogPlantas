from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from problemas.forms import ProblemaCustom
from problemas.models import Problema
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
# PROBLEMAS

class ProblemListView(ListView):
    model = Problema
    template_name = 'problemas/problemas_list.html'

class ProblemDetailView(DetailView):
    model = Problema
    template_name = 'problemas/problema_detalle.html'

class ProblemCreateView(LoginRequiredMixin, CreateView):
    model = Problema
    success_url = reverse_lazy('problemas:ListaProblemas')
    form_class = ProblemaCustom
    # fields = ['nombreProblema','nombreCientifico','peligro','productos','solucion', 'imagen']
    def get_template_names(self):         
        return 'problemas/problema_form.html'

class ProblemUpdateView(LoginRequiredMixin, UpdateView):
    model = Problema
    success_url = reverse_lazy('problemas:ListaProblemas')
    form_class = ProblemaCustom
    # fields = ['nombreProblema','nombreCientifico','peligro','productos','solucion', 'imagen']
    def get_template_names(self):         
        return 'problemas/problema_form.html'

class ProblemDeleteView(LoginRequiredMixin, DeleteView):
    model = Problema
    success_url = reverse_lazy('problemas:ListaProblemas')
    def get_template_names(self):         
        return 'problemas/problema_confirm_delete.html'
