from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contacto/contacto.html')
