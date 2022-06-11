from django.urls import path
from django.contrib.auth.views import LogoutView
from sesion import views


app_name='sesion'
urlpatterns = [
    # PLANTAS
    path('login', views.login_request, name='Login'),
    path('<int:pk>/perfil', views.Perfil.as_view(), name='Perfil'),
    path('editarPerfil', views.editar_perfil, name='EditarPerfil'),
    path('logout', LogoutView.as_view(template_name='sesion/logout.html'), name='Logout'),
    path('avatar/', views.CreateAvatarView.as_view(), name='Avatar'),
    path('avatar/<int:pk>/update/', views.UpdateAvatarView.as_view(), name='UpdateAvatar'),
        
    ]
    # Almlm23423 9787LKGLKGlg