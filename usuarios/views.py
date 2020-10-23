from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from pagbase.urls import paginaprincipal
from .forms import inicioForm
# Create your views here.
def iniciarSesion(request):
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
                return redirect('') 
    context = {
        'formulario2':formulario
    }
    return render(
        request,
        'usuario/login.html',
        context
    )
def registro(request):
    formulario = inicioForm()
    if request.method == 'POST':
        formulario = inicioForm(data = request.POST)
        if formulario.is_valid():
            usuarioRegistrado = formulario.save()
            if usuarioRegistrado is not None:
                login(request, usuarioRegistrado)
                return redirect('/accounts/perfil/')
    context ={
        'formulario':formulario
    }
    return render(
        request,
        'usuario/registro.html',
        context
    )
def salir(request):
    logout(request)
    return redirect(to='/')

def perfil(request):
    if request.user.is_authenticated:
        return render(
            request,
            'usuario/perfil.html'
        )
    return redirect(to='/')