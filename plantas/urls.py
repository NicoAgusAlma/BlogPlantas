from django.urls import path

from plantas import views


app_name='plantas'
urlpatterns = [
    # PLANTAS
    path('list/', views.PlantListView.as_view(), name='ListaPlantas'),
    path('add/', views.PlantCreateView.as_view(), name='AgregarPlanta'),
    path('<int:pk>/detail/', views.PlantDetailView.as_view(), name='DetallePlanta'),
    path('<int:pk>/update/', views.PlantUpdateView.as_view(), name='UpdatePlanta'),
    path('<int:pk>/delete/', views.PlantDeleteView.as_view(), name='BorrarPlanta'),
    path('ui/', views.ui, name='Ui'),
   
   ]