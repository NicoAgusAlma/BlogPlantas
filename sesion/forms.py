from email.mime import image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from sesion.models import Avatar

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text="Contraloca")
    password2= forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
   
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields['password1'].label = 'Contraseña'
            self.fields['password2'].label = 'Repetir contraseña'
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        help_texts = {k:'' for k in fields}

# class UserEditForm(UserCreationForm):
#     email=forms.EmailField(label='Modificar eMail')
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['email', 'password1', 'password2']
#         help_texts = {k:'' for k in fields}

# Mike3455 AKJAlkjsjj23423

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = Avatar

#     def clean_avatar(self):
#         avatar = self.cleaned_data['avatar']
#         return avatar




class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name' ]
        # widgets = {
        #     'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        # }