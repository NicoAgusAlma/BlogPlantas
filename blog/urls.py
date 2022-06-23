from django.urls import path

from blog import views


app_name='blog'
urlpatterns = [
    # BLOG
    path('list/', views.PostListView.as_view(), name='ListaPosteos'),
    path('add/', views.PostCreateView.as_view(), name='AgregarPosteo'),
    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='DetallePosteo'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='UpdatePosteo'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='BorrarPosteo'),
    path('categoria/<str:cate>', views.CategoryCustomList, name='ListaCategoria'),

    # LISTADO DE CATEGORIAS
    path('categorias/', views.CategoriesListView.as_view(), name='ListaCategorias'),
    path('categoria/add/', views.CategoryCreateView.as_view(), name='AgregarCategoria'),
    path('categoria/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='UpdateCategoria'),
    path('categoria/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='BorrarCategoria'),

    # COMENTARIOS
    path('<int:pk>/detail/comentar/', views.ComentCreateView.as_view(), name='AgregarComentario'),
    path('<int:pk>/comentario/eliminar/', views.ComentDeleteView.as_view(), name='EliminarComentario'),

   ]
  
    # HACER CARGA INICIAL DE DATOS
    # HACER TESTING
    # HACER README
    # VER BIBLIOTECAS INSTALADAS
    
   