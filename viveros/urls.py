from django.urls import path

from viveros import views


app_name='viveros'
urlpatterns = [   
    # VIVEROS
    path('list/', views.GreenHouseListView.as_view(), name='ListaViveros'),
    path('add/', views.GreenHouseCreateView.as_view(), name='AgregarVivero'),
    path('<int:pk>/detail/', views.GreenHouseDetailView.as_view(), name='DetalleVivero'),
    path('<int:pk>/update/', views.GreenHouseUpdateView.as_view(), name='UpdateVivero'),
    path('<int:pk>/delete/', views.GreenHouseDeleteView.as_view(), name='BorrarVivero'),

]