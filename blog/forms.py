
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from blog.models import Posteo, Comentario, Categoria

cat = Categoria.objects.all().values_list('nombre', 'nombre')
choice_list = []
for item in cat:
    choice_list.append(item)

class BlogPost(forms.ModelForm):
    class Meta:
        model=Posteo
        fields = ('titulo','subtitulo','autor', 'texto', 'categoria', 'imagen')
        widgets = {
            'autor': forms.TextInput(attrs={'palceholder':'user name', 'id':'usuarioImagen', 'type':'hidden'}),
            'categoria': forms.Select(choices=choice_list),
        }

class Comentar(forms.ModelForm):
    class Meta:
        model=Comentario
        fields = ('nombre','texto')
        widgets = {
            'nombre': forms.TextInput(attrs={'palceholder':'user name', 'id':'comentar', 'type':'hidden'}),
            
        }
        