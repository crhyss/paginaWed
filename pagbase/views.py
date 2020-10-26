from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Producto
from .forms import ProductoForm
def paginaprincipal(request):
    formulario = AuthenticationForm()
    usuario =AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username = username,password = password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                return redirect('/') 
    context = {
        'titulo':'Tiendita del Cris',
        'formulario2':formulario
    }
    return render(
        request,
        'pagbase/principal.html',
        context
    )   
def agregarProducto(request):
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/principal/listar/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo':'Agregar Producto',
        'formulario':formulario
    }    
    return render(
        request,
        'pagbase/agregar.html',
        context
    )
def modificarProducto(request,id_producto):
    productoRecibido = Producto.objects.get(pk=id_producto)
    formulario = None
    if request.method =='POST':
        formulario = ProductoForm(request.POST, instance=productoRecibido)
        if formulario.is_valid():
            formulario.save()
            return redirect('/principal/listar/')
    else:
        formulario = ProductoForm(instance=productoRecibido)
    context = {
        'titulo':'Modificar Producto',
        'formulario':formulario
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
def eliminarProducto(request,id_producto):
    productoEliminado = Producto.objects.get(pk = id_producto)
    productoEliminado.delete()
    return (redirect('/principal/listar/'))

