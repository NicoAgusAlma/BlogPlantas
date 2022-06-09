from django.urls import path

from plantas import views


app_name='plantas'
urlpatterns = [
    # PLANTAS
    path('list/', views.PlantaList.as_view(), name='ListaPlantas'),
    path('add/', views.PlantaCreate.as_view(), name='AgregarPlanta'),
    path('<int:pk>/detail/', views.PlantaDetail.as_view(), name='DetallePlanta'),
    path('<int:pk>/update/', views.PlantaUpdate.as_view(), name='UpdatePlanta'),
    path('<int:pk>/delete/', views.PlantaDelete.as_view(), name='BorrarPlanta'),
   ]