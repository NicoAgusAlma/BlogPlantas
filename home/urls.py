from django.urls import path

from home import views

app_name='home'
urlpatterns = [
    # HOME
    path('', views.inicio, name='Inicio'),
    
   ]