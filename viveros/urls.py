from django.urls import path

from viveros import views


app_name='viveros'
urlpatterns = [   
    # VIVEROS
    path('list/', views.ViveroList.as_view(), name='ListaViveros'),
    path('add/', views.ViveroCreate.as_view(), name='AgregarVivero'),
    path('<int:pk>/detail/', views.ViveroDetail.as_view(), name='DetalleVivero'),
    path('<int:pk>/update/', views.ViveroUpdate.as_view(), name='UpdateVivero'),
    path('<int:pk>/delete/', views.ViveroDelete.as_view(), name='BorrarVivero'),

]