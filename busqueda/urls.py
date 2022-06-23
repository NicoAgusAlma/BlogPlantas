from django.urls import path

from busqueda import views


app_name='busqueda'
urlpatterns = [
    # BUSCADOR
    path('buscar/', views.search),
    path('buscador/', views.explorer, name='Buscador'),
    ]