from traceback import format_list
from django.forms import TextInput
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.forms import BlogPost
from blog.models import Posteo
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from plantas.models import Planta
from django.contrib.auth.models import User

# Create your views here.
class PosteoList(ListView):
    model = Posteo
    template_name = 'blog/posteos_list.html'
    plant_list = Planta.objects.all()
    usuarios = User.objects.all()
    extra_context= {'plant_list':plant_list, 'usuarios':usuarios}

class PosteoDetail(DetailView):
    model = Posteo
    template_name = 'blog/posteo_detalle.html'

class PosteoCreate(LoginRequiredMixin, CreateView):
    model = Posteo
    success_url = reverse_lazy('blog:ListaPosteos')
    form_class = BlogPost
    def get_template_names(self):         
        return 'blog/posteo_form.html'
    
class PosteoUpdate(LoginRequiredMixin, UpdateView):
    model = Posteo
    form_class = BlogPost
    success_url = reverse_lazy('blog:ListaPosteos')
    def get_template_names(self):         
        return 'blog/posteo_form.html'

class PosteoDelete(LoginRequiredMixin, DeleteView):
    model = Posteo
    success_url = reverse_lazy('blog:ListaPosteos')
    def get_template_names(self):         
        return 'blog/posteo_confirm_delete.html'

