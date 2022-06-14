
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from sesion.models import Avatar

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text='<br>La contraseña debe tener minimo 8 caracteres, 1 minuscula y 1 mayuscula y diferente a los campos anteriores')
    password2= forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
   # asdfa4t24awg4 KHG729sdiusd
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {k:'' for k in fields}

class AvatarUser(forms.ModelForm):
    class Meta:
        model=Avatar
        fields = ('user','imagen')
        widgets = {
            'user': forms.TextInput(attrs={'palceholder':'user name', 'id':'usuarioImagen', 'type':'hidden'}),
        }

class UserEditForm(UserChangeForm):
    password = None    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email' ]
        