from django.shortcuts import render, redirect
from pagbase.models import Producto
from django.contrib.auth.decorators import login_required
from .cart import Cart

# Create your views here.
@login_required(redirect_field_name='login')
def agregarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id = producto_id)
    cart.add(producto = producto)
    return redirect('/carrito/')
@login_required(login_url="/accounts/login/")
def eliminarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id = producto_id)
    cart.remove(producto)
    return redirect("/carrito/")
@login_required(login_url="/accounts/login/")
def decrementarProducto(request, producto_id):
    cart = Cart(request)
    producto = Producto.objects.get(id = producto_id)
    cart.decrement(producto = producto)
    return redirect("/carrito/")
@login_required(login_url="/accounts/login/")
def limpiarCarrito(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/carrito/")