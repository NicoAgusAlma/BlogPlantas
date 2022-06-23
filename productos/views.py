from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from productos.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
# PRODUCTOS

class ProductListView(ListView):
    model = Producto
    template_name = 'productos/productos_list.html'

class ProductDetailView(DetailView):
    model = Producto
    template_name = 'productos/producto_detalle.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    fields = ['nombre','precio','puntoDeVenta', 'imagen']
    def get_template_names(self):         
        return 'productos/producto_form.html'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    fields = ['nombre','precio','puntoDeVenta', 'imagen']
    def get_template_names(self):         
        return 'productos/producto_form.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:ListaProductos')
    def get_template_names(self):         
        return 'productos/producto_confirm_delete.html'