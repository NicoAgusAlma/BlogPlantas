from django.urls import path

from contacto import views


app_name='contacto'
urlpatterns = [
    #CONTACTO
    path('contacto', views.contacto, name='Contacto'),

    ]