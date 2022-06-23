from django.urls import path

from problemas import views


app_name='problemas'
urlpatterns = [
    # PROBLEMAS
    path('list/', views.ProblemListView.as_view(), name='ListaProblemas'),
    path('add/', views.ProblemCreateView.as_view(), name='AgregarProblema'),
    path('<int:pk>/detail/', views.ProblemDetailView.as_view(), name='DetalleProblema'),
    path('<int:pk>/update/', views.ProblemUpdateView.as_view(), name='UpdateProblema'),
    path('<int:pk>/delete/', views.ProblemDeleteView.as_view(), name='BorrarProblema'),
   
   ]