from django.urls import path
from django.contrib.auth.views import LogoutView
from sesion import views


app_name='sesion'
urlpatterns = [
    # PLANTAS
    path('login', views.login_request, name='Login'),
    path('logout', LogoutView.as_view(template_name='sesion/logout.html'), name='Logout'),
        
    ]