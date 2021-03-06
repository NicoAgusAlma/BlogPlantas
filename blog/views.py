from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.forms import BlogPost, Comentar
from blog.models import Posteo, Comentario, Categoria
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from plantas.models import Planta
from django.contrib.auth.models import User


class PosteoList(ListView):
    model = Posteo
    template_name = 'blog/posteos_list.html'
    ordering = ['-fecha']
    plant_list = Planta.objects.all()
    usuarios = User.objects.all()
    categorias = Categoria.objects.all()
    extra_context= {'plant_list':plant_list, 'usuarios':usuarios, 'categorias':categorias } 


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

def CategoriaList(request, cate):
    posteos_filtrados = Posteo.objects.filter(categoria=cate)
    categorias = Categoria.objects.all()
    posteos = Posteo.objects.all()
    return render (request , 'blog/posteos_filtrados.html', {'posteos_filtrados': posteos_filtrados, 'cate':cate, 'posteos':posteos, 'categorias':categorias})

class CategoriasList(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'blog/categorias_list.html'

class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    success_url = reverse_lazy('blog:ListaCategorias')
    fields = ['nombre']
    def get_template_names(self):         
        return 'blog/categorias_form.html'

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    success_url = reverse_lazy('blog:ListaCategorias')
    fields = ['nombre']
    def get_template_names(self):         
        return 'blog/categorias_form.html'

class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy('blog:ListaCategorias')
    def get_template_names(self):         
        return 'blog/categorias_confirm_delete.html'

class ComentarioCreate(LoginRequiredMixin, CreateView):
    model = Comentario
    success_url = reverse_lazy('blog:ListaPosteos')
    form_class = Comentar

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_template_names(self):         
        return 'blog/comentario_form.html'

    def get_success_url(self):
          postID=self.kwargs['pk']
          return reverse_lazy('blog:DetallePosteo', kwargs={'pk': postID})

class ComentarioDelete(LoginRequiredMixin, DeleteView):
    model = Comentario
    
    def get_template_names(self):         
        return 'blog/comentario_confirm_delete.html'    

    def get_success_url(self):        
        posteo = Comentario.objects.all()[0]
        posteoID = posteo.post_id
        return reverse_lazy('blog:DetallePosteo', kwargs={'pk': posteoID})