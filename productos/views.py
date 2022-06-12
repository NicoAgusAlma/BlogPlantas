from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from productos.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# PRODUCTOS

class ProductoList(ListView):
    model = Producto
    template_name = 'productos/productos_list.html'

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'productos/producto_detalle.html'

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    fields = ['nombre','precio','puntoDeVenta', 'imagen']
    def get_template_names(self):         
        return 'productos/producto_form.html'

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    fields = ['nombre','precio','puntoDeVenta', 'imagen']
    def get_template_names(self):         
        return 'productos/producto_form.html'

class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    def get_template_names(self):         
        return 'productos/producto_confirm_delete.html'