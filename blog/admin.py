from django.contrib import admin
from blog.models import Posteo, Categoria, Comentario

# Register your models here.
admin.site.register(Posteo)
admin.site.register(Categoria)
admin.site.register(Comentario)