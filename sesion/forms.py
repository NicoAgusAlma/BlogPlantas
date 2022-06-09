from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password: forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text="Contraloca")
    password1: forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['password1'].label = 'Contraseña'
            self.fields['password2'].label = 'Repetir contraseña'
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','last_name','email','password1','password2']
        help_texts = {k:'' for k in fields}