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
    path('categoria/<str:cate>', views.CategoriaList, name='ListaCategoria'),

    # LISTADO DE CATEGORIAS
    path('categorias/', views.CategoriasList.as_view(), name='ListaCategorias'),
    path('categoria/add/', views.CategoriaCreate.as_view(), name='AgregarCategoria'),
    path('categoria/<int:pk>/update/', views.CategoriaUpdate.as_view(), name='UpdateCategoria'),
    path('categoria/<int:pk>/delete/', views.CategoriaDelete.as_view(), name='BorrarCategoria'),

   ]
  
   # VER LO DE LOS COMENTARIOS EN LOS POSTEOS!!!
   