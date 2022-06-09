from django.shortcuts import render
from BlogPlantas.forms import PosteoFormulario, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


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
                return render(request, 'home/inicio.html', {'mensaje':f', Bienvenido {usuario}'})
            else:
                return render(request, 'home/inicio.html', {'mensaje':', Error, datos incorrectos'})
        elif form2.is_valid:
            try:
                form2.save()
                return render(request=request, 
                template_name='home/inicio.html', 
                context={'mensaje':', Usuario creado'})
            except:
                return render(request, 'sesion/error_registro.html', {'mensaje':', Error, formulario erroneo'})
        else:
            return render(request, 'home/inicio.html', {'mensaje':', Error, formulario erroneo'})
    form = AuthenticationForm()
    form2=UserRegisterForm()
    return render(request, 'sesion/login.html', {'form':form, 'form2':form2})
