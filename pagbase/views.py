from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.
from .models import Producto, Categoria
from .forms import ProductoForm, CategoriaForm
from usuarios.forms import inicioForm
from carrito.cart import Cart
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required

def paginaprincipal(request):
    cart = Cart(request)
    formulario = AuthenticationForm()
    usuario = AuthenticationForm()
    lista = Categoria.objects.all()
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            usuarioLogeado = authenticate(username=username, password=password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                if usuarioLogeado.username == 'admin':
                    return redirect('/administracion/')
                else:
                    return redirect('/')
    context = {
        'titulo': 'Tiendita del Cris',
        'formulario2': formulario,
        'lista': lista
    }
    return render(
        request,
        'pagbase/principal.html',
        context
    )

@permission_required('view_group')
def agregarProducto(request):
    lista = Categoria.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/')
    else:
        formulario = ProductoForm()
    context = {
        'titulo': 'Agregar Producto',
        'formulario': formulario,
        'lista': lista,
    }
    return render(
        request,
        'pagbase/agregar.html',
        context
    )
@permission_required('change_producto')
def modificarProducto(request, id_producto):
    productoRecibido = Producto.objects.get(pk=id_producto)
    lista = Categoria.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance=productoRecibido)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listar/')
    else:
        formulario = ProductoForm(instance=productoRecibido)
    context = {
        'titulo': 'Modificar Producto',
        'formulario': formulario,
        'lista': lista,
    }
    return render(
        request,
        'pagbase/modificar_t.html',
        context
    )

@permission_required('view_producto')
def listarProducto(request):
    productos = Producto.objects.all()
    lista = Categoria.objects.all()
    context = {
        'titulo': 'Productos',
        'productos': productos,
        'lista': lista,
    }
    return render(
        request,
        'pagbase/listarTecnologia.html',
        context
    )

@permission_required('delete_producto')
def eliminarProducto(request, id_producto):
    productoEliminado = Producto.objects.get(pk=id_producto)
    productoEliminado.delete()
    return (redirect('/listar/'))

@permission_required('view_producto')
def administracion(request):
    lista = Categoria.objects.all()
    context = {
        'titulo': 'Administrador',
        'lista': lista,
    }
    return render(
        request,
        'admin/admin.html',
        context
    )


def lista(request, id):
    cart = Cart(request)
    productos = Producto.objects.filter(categoria_id__exact=id)
    formulario2 = AuthenticationForm()
    lista = Categoria.objects.all()
    if request.method == 'POST':
        formulario2 = AuthenticationForm(data=request.POST)
        if formulario2.is_valid():
            username = formulario2.cleaned_data['username']
            password = formulario2.cleaned_data['password']
            usuarioLogeado = authenticate(username=username, password=password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                return redirect('/')
        
    paginator = Paginator(productos, 6)
    page = request.GET.get('page')
    productos = paginator.get_page(page)

    context = {
        'titulo': 'lista',
        'productos': productos,
        'formulario2': formulario2,
        'lista':lista
    }
    return render(
        request,
        'pagbase/catalogoModa.html',
        context
    )



def muestraProducto(request, id_producto):
    lista = Categoria.objects.all()
    productoRecibido = Producto.objects.get(pk=id_producto)
    formulario2 = AuthenticationForm()
    if request.method == 'POST':
        formulario2 = AuthenticationForm(data=request.POST)
        if formulario2.is_valid():
            username = formulario2.cleaned_data['username']
            password = formulario2.cleaned_data['password']
            usuarioLogeado = authenticate(username=username, password=password)
            if usuarioLogeado is not None:
                login(request, usuarioLogeado)
                return redirect('/')
    context = {
        'titulo': 'Productos',
        'producto': productoRecibido,
        'lista': lista,
        'formulario2': formulario2,
    }
    return render(
        request,
        'pagbase/datosProductos.html',
        context
    )

@permission_required('view_producto')
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
        'titulo': 'Agregar Categoria',
        'formularioC': formulario,
        'lista': lista,
        'usuario': usuario,

    }
    return render(
        request,
        'admin/categoria.html',
        context
    )
def carrito(request):
    lista = Categoria.objects.all()
    usuario = AuthenticationForm()
    context = {
        'titulo': 'Carrito',
        'lista': lista,
        'usuario': usuario,
    }    
    return render(
        request,
        'pagbase/carrito.html',
        context
    )

def offline(request):
    lista = Categoria.objects.all()
    usuario = AuthenticationForm()
    context = {
        'titulo': 'offline',
        'lista': lista,
        'usuario': usuario,
    }    
    return render(
        request,
        'offline.html',
        context
    )

def listarCategorias(request):
    categorias = Categoria.objects.all()
    lista = Categoria.objects.all()
    context = {
        'titulo':'Categorías',
        'categorias': categorias,
        'lista': lista
    }
    return render(
        request,
        'pagbase/listarCategorias.html',
        context
    )

def modificarCategoria(request, id):
    categoria = Categoria.objects.get(pk = id)
    lista = Categoria.objects.all()
    formulario = None
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance = categoria)
        if formulario.is_valid():
            formulario.save()
            return redirect('/listacategorias/')
    else:
        formulario = CategoriaForm(instance = categoria)
    context = {
        'titulo': 'Modificar categoría',
        'formulario': formulario,
        'lista': lista
    }
    return render(
        request,
        'pagbase/modificarCategoria.html',
        context
    )

def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(pk = id)
    categoria.delete()
    return redirect('/listacategorias/')