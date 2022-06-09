from django.urls import path

from galeria import views


app_name='galeria'
urlpatterns = [
    #GALERIA
    path('', views.Galeria.as_view(), name='Galeria'),
    ]