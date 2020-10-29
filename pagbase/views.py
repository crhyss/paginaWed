from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Producto,Categoria
from .forms import ProductoForm,CategoriaForm

def paginaprincipal(request):
    formulario = AuthenticationForm()
    usuario =AuthenticationForm()
    lista = Categoria.objects.all()
    if request.method == 'POST':
        formulario = AuthenticationForm(data = request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username = username,password = password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                if usuarioLogeado.username == 'admin':
                    return redirect('/administracion/')
                else:
                    return redirect('/')
    context = {
        'titulo':'Tiendita del Cris',
        'formulario2':formulario,
        'lista':lista
    }
    return render(
        request,
        'pagbase/principal.html',
        context
    )   
def agregarProducto(request):
    lista = Categoria.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo':'Agregar Producto',
        'formulario':formulario,
        'lista':lista,
    }    
    return render(
        request,
        'pagbase/agregar.html',
        context
    )
def modificarProducto(request,id_producto):
    productoRecibido = Producto.objects.get(pk=id_producto)
    lista = Categoria.objects.all()
    formulario = None
    if request.method =='POST':
        formulario = ProductoForm(request.POST, instance=productoRecibido)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/')
    else:
        formulario = ProductoForm(instance=productoRecibido)
    context = {
        'titulo':'Modificar Producto',
        'formulario':formulario,
        'lista':lista,
    }    
    return render(
        request,
        'pagbase/modificar_t.html',
        context
    )
def listarProducto(request):
    productos = Producto.objects.all()
    lista = Categoria.objects.all()
    context = {
        'titulo':'Productos',
        'productos':productos,
        'lista':lista,
    }    
    return render(
        request,
        'pagbase/listarTecnologia.html',
        context
    )
def eliminarProducto(request,id_producto):
    productoEliminado = Producto.objects.get(pk = id_producto)
    productoEliminado.delete()
    return (redirect('/listar/'))

def administracion(request):
    lista = Categoria.objects.all()
    context = {
        'titulo':'Administrador',
        'lista':lista,
    }   
    return render(
        request,
        'admin/admin.html',
        context
    )
def lista(request,id):
    usuario = AuthenticationForm()
    lista = Categoria.objects.all()
    productos = Producto.objects.filter(categoria_id__exact = id)
    context = {
        'titulo':'lista',
        'usuario':usuario,
        'productos':productos,
        'lista':lista,
        'usuario':usuario
    }   
    return render(
        request,
        'pagbase/catalogoModa.html',
        context
    )

def muestraProducto(request,id_producto):
    lista = Categoria.objects.all()
    usuario = AuthenticationForm()
    productoRecibido = Producto.objects.get(pk=id_producto)
    context = {
        'titulo':'Moda',
        'producto':productoRecibido,
        'usuario':usuario,
        'lista':lista,
    }    
    return render(
        request,
        'pagbase/datosProductos.html',
        context
    )
def categoria(request):
    usuario = AuthenticationForm()
    lista = Categoria.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('/')
    else:
        formulario = CategoriaForm()
    context = {
        'titulo':'Agregar Categoria',
        'formularioC':formulario,
        'lista':lista,
        'usuario':usuario,
        
    }    
    return render(
        request,
        'admin/categoria.html',
        context
    )