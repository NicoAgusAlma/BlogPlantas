from email.mime import image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from blog.models import Posteo

class BlogPost(forms.ModelForm):
    class Meta:
        model=Posteo
        fields = ('titulo','subtitulo','autor','fecha', 'texto', 'imagen')
        widgets = {
            'autor': forms.TextInput(attrs={'palceholder':'user name', 'id':'usuarioImagen', 'type':'hidden'}),
        }