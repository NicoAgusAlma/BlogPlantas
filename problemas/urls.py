from django.urls import path

from problemas import views


app_name='problemas'
urlpatterns = [
    # PROBLEMAS
    path('list/', views.ProblemaList.as_view(), name='ListaProblemas'),
    path('add/', views.ProblemaCreate.as_view(), name='AgregarProblema'),
    path('<int:pk>/detail/', views.ProblemaDetail.as_view(), name='DetalleProblema'),
    path('<int:pk>/update/', views.ProblemaUpdate.as_view(), name='UpdateProblema'),
    path('<int:pk>/delete/', views.ProblemaDelete.as_view(), name='BorrarProblema'),
   
   ]