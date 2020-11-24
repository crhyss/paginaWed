from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth import login, logout, authenticate
from pagbase.urls import paginaprincipal
from .forms import inicioForm
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generador
from django.views import View
from pagbase.models import Categoria
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from carrito.cart import Cart

# Create your views here.


def iniciarSesion(request):
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
        'usuario/login copy.html',
        context
    )


def registro(request):
    lista = Categoria.objects.all()
    formulario = inicioForm()
    formulario.fields['username'].help_text = None
    formulario.fields['password1'].help_text = None
    formulario.fields['password2'].help_text = None
    formulario.fields['genero']
    formulario2 = AuthenticationForm()
    usuario = AuthenticationForm()
    if request.method == 'POST':
        formulario = inicioForm(data=request.POST)
        if formulario.is_valid():
            usuarioRegistrado = formulario.save(commit=False)   
            usuarioRegistrado.is_active = False
            usuarioRegistrado.save()
            uidb64 = urlsafe_base64_encode(force_bytes(usuarioRegistrado.pk))
            dominio = get_current_site(request).domain
            link = reverse('activacion', kwargs={
                           'uidb64': uidb64, 'token': token_generador.make_token(usuarioRegistrado)})
            exito = messages.success(request, 'cuenta creada con exito')
            asunto = 'Confirmacion de usuario'
            activar_url = 'http://'+dominio+link
            mensaje = 'Hola '+usuarioRegistrado.username + \
                ', gracias por registrarte en La tiendita de cristian, porfavor usa este link de verificacion para confirmar tu cuenta\n' + activar_url
            correo = EmailMessage(asunto, mensaje, to=[
                                  formulario.cleaned_data['email']])
            correo.send()
            if usuarioRegistrado is not None:
                login(request, usuarioRegistrado)
                return redirect('/')
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
        'formulario': formulario,
        'formulario2': formulario2,
        'lista':lista
    }
    return render(
        request,
        'usuario/registro.html',
        context
    )


def salir(request):
    logout(request)
    return redirect(to='/accounts/login')

@login_required(login_url='/accounts/login/')
def perfil(request):
    cart = Cart(request)
    lista = Categoria.objects.all()
    context = {
    'lista':lista
    }
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            return render(
                request,
                'admin/admin.html',
                context
        )
        else:
            return render(
                request,
                'usuario/perfil.html',
                context
        )

class verificacion(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            usuario = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            usuario = None

        if usuario is not None and token_generador.check_token(usuario, token):
            usuario.is_active = True
            usuario.save()
            login(request, usuario)
            messages.success(request, ('Tu cuenta ha sido confirmada.'))
            return redirect('/')
        else:
            messages.warning(request, ('La confirmación de la cuenta es invalida, posiblemente porque ya se ha utilizado.'))
            return redirect('/')

class restablecerContasenia(PasswordResetView):
    template_name = 'usuario/cambiocontrasenia.html'
    success_url='/'
