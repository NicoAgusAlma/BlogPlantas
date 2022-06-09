from django.urls import path

from productos import views


app_name='productos'
urlpatterns = [
    # PRODUCTOS
    path('list/', views.ProductoList.as_view(), name='ListaProductos'),
    path('add/', views.ProductoCreate.as_view(), name='AgregarProducto'),
    path('<int:pk>/detail/', views.ProductoDetail.as_view(), name='DetalleProducto'),
    path('<int:pk>/update/', views.ProductoUpdate.as_view(), name='UpdateProducto'),
    path('<int:pk>/delete/', views.ProductoDelete.as_view(), name='BorrarProducto'),
   
   ]