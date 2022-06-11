from re import A
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.forms.models import model_to_dict
from requests import request
from sesion.forms import AvatarUser, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from sesion.forms import UserEditForm
from sesion.models import Avatar
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here. 
def login_request(request):
    if request.method == 'POST':
        form=AuthenticationForm(request, data=request.POST)
        form2 = UserRegisterForm(request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user=authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return render(request, 'home/mensaje.html', {'mensaje_titulo':usuario,'mensaje': 'Bienvenido'})
            else:
                return render(request, 'home/mensaje.html', {'mensaje_titulo':'Error','mensaje': 'Datos Incorrectos'})
        elif form2.is_valid:
            try:
                form2.save()
                return render(request=request, 
                template_name='home/mensaje.html', 
                context={'mensaje':'Usuario creado, por favor, inicie sesion.'})
            except:
                return render(request, 'home/mensaje.html', {'mensaje_titulo':'Error','mensaje': 'Formulario erroneo'})
        else:
            return render(request, 'home/mensaje.html', {'mensaje_titulo':'Error','mensaje': 'Formulario erroneo'})
    form = AuthenticationForm()
    form2=UserRegisterForm()
    return render(request, 'sesion/login.html', {'form':form, 'form2':form2})

def editar_perfil(request):
    user = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return render(request, 
            'home/mensaje.html', 
            {'mensaje':'Usuario modificado correctamente.', 
            'mensaje_titulo':'Modificacion de Usuario'})

    form= UserEditForm(model_to_dict(user))
    return render(
        request=request,
        context={'form': form},
        template_name="sesion/editar_perfil.html",
    )

class Perfil(ListView):
    model = User
    template_name = 'sesion/perfil.html'

class CreateAvatarView(CreateView):
    model=Avatar
    form_class=AvatarUser
    template_name = 'sesion/avatar.html'
    success_url = reverse_lazy('sesion:Perfil')

class UpdateAvatarView(UpdateView):
    model=Avatar
    form_class=AvatarUser
    success_url = reverse_lazy('sesion:Perfil')
    def get_template_names(self):         
        return 'sesion/avatar.html'

def get_avatar(request):   
    avatars=Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        print('Listo')
        return {'url':avatars[0].imagen.url}
    return {}

def perfil(request):
    return render (request, 'sesion/perfil.html')

    