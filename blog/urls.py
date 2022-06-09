from django.urls import path

from blog import views


app_name='blog'
urlpatterns = [
    # BLOG
    path('list/', views.PosteoList.as_view(), name='ListaPosteos'),
    path('add/', views.PosteoCreate.as_view(), name='AgregarPosteo'),
    path('<int:pk>/detail/', views.PosteoDetail.as_view(), name='DetallePosteo'),
    path('<int:pk>/update/', views.PosteoUpdate.as_view(), name='UpdatePosteo'),
    path('<int:pk>/delete/', views.PosteoDelete.as_view(), name='BorrarPosteo'),

   ]