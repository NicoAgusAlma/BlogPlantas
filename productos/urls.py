from django.urls import path

from productos import views


app_name='productos'
urlpatterns = [
    # PRODUCTOS
    path('list/', views.ProductListView.as_view(), name='ListaProductos'),
    path('add/', views.ProductCreateView.as_view(), name='AgregarProducto'),
    path('<int:pk>/detail/', views.ProductDetailView.as_view(), name='DetalleProducto'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='UpdateProducto'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='BorrarProducto'),
   
   ]