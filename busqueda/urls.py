from django.urls import path

from busqueda import views


app_name='busqueda'
urlpatterns = [
    # BUSCADOR
    path('buscar/', views.buscar),
    path('buscador/', views.buscador, name='Buscador'),
    ]