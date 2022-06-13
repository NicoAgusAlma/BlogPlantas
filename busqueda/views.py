from django.shortcuts import render
from django.db.models import Q
from blog.models import Posteo
# from plantas.models import Planta
from viveros.models import Vivero
from productos.models import Producto
from problemas.models import Problema


# Create your views here.


def buscador(request):
    return render(request, 'busqueda/resultado_busqueda.html',{'search_param':''})


def buscar(request):
    if request.GET['busqueda']:
        search_param = request.GET['busqueda']
        print(search_param)
        # query = Q(nombreComun__contains=search_param)
        # query.add(Q(nombreCientifico__contains=search_param), Q.OR)
        # query.add(Q(familia__contains=search_param), Q.OR)
        # query.add(Q(sustrato__contains=search_param), Q.OR)
        # query.add(Q(viveros__contains=search_param), Q.OR)
        # query.add(Q(peligrosComunes__contains=search_param), Q.OR)
        # plantas = Planta.objects.filter(query)
        query = Q(nombreProblema__contains=search_param)
        query.add(Q(nombreCientifico__contains=search_param), Q.OR)
        query.add(Q(peligro__contains=search_param), Q.OR)
        query.add(Q(productos__contains=search_param), Q.OR)
        query.add(Q(solucion__contains=search_param), Q.OR)        
        problemas = Problema.objects.filter(query)
        query = Q(nombre__contains=search_param)
        query.add(Q(provincia__contains=search_param), Q.OR)
        query.add(Q(localidad__contains=search_param), Q.OR)
        query.add(Q(calle__contains=search_param), Q.OR)
        query.add(Q(stockPlantas__contains=search_param), Q.OR)        
        query.add(Q(stockProductos__contains=search_param), Q.OR)             
        viveros = Vivero.objects.filter(query)
        query = Q(nombre__contains=search_param)
        query.add(Q(solucionaProblemas__contains=search_param), Q.OR)
        query.add(Q(puntoDeVenta__contains=search_param), Q.OR)               
        productos = Producto.objects.filter(query)            
        query = Q(titulo__contains=search_param)        
        query.add(Q(subtitulo__contains=search_param), Q.OR)
        query.add(Q(texto__contains=search_param), Q.OR)               
        query.add(Q(autor__username__contains=search_param), Q.OR)               
        posteos = Posteo.objects.filter(query)
        context_dict = {
            'search_param':search_param,
            #'plantas': plantas,
            'problemas': problemas,
            'viveros':viveros,
            'productos':productos,
            'posteos':posteos
        }
        
        return render(
            request=request,
            context=context_dict,
            template_name="busqueda/resultado_busqueda.html",
        )
    else:

        respuesta = 'No ingresó ningun dato' 

        return render(request, 'busqueda/resultado_busqueda.html', {'respuesta':respuesta})
    