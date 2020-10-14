from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.
from .models import Producto
from .forms import ProductoForm
def paginaprincipal(request):
    context = {
        'titulo':'Tiendita del Cris'
    }
    return render(
        request,
        'pagbase/principal.html',
        context
    )   
def agregarProducto(request):
    context = {
        'titulo':'Agregar Producto'
    }    
    return render(
        request,
        'pagbase/agregar.html',
        context
    )
def modificarProducto(request,id_producto):
    context = {
        'titulo':'Modificar Producto'
    }    
    return render(
        request,
        'pagbase/modificar_t.html',
        context
    )
def listarProducto(request):
    productos = Producto.objects.all()
    context = {
        'titulo':'Productos',
        'productos':productos
    }    
    return render(
        request,
        'pagbase/listarTecnologia.html',
        context
    )