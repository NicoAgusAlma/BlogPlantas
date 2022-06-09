from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('home.urls')),
    path('BlogPlantas/', include('BlogPlantas.urls')),
    path('plantas/', include('plantas.urls')),
    path('sesion/', include('sesion.urls')),
    path('viveros/', include('viveros.urls')),
    path('productos/', include('productos.urls')),
    path('problemas/', include('problemas.urls')),
    path('blog/', include('blog.urls')),
    path('galeria/', include('galeria.urls')),
    path('contacto/', include('contacto.urls')),
    path('busqueda/', include('busqueda.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
