from django.urls import path
from .views import iniciarSesion,registro,salir,perfil,verificacion,restablecerContasenia, listarUsuarios,eliminarUsuario, agregarGenero, listarGeneros,modificarGenero, eliminarGenero
from django.contrib.auth import views as auth_views
from usuarios import views
# from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/',iniciarSesion, name='iniciarSesion'),
    path('registro/',registro, name='registro'),
    path('salir/',salir, name='salir'),
    path('perfil/',perfil, name='perfil'),
    path('activacion/<uidb64>/<token>',verificacion.as_view(), name='activacion'),
     path('password-reset/',auth_views.PasswordResetView.as_view(template_name='usuario/cambiocontrasenia.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='usuario/reset.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='usuario/confirmacion.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='usuario/registrocompleto.html'
         ),
         name='password_reset_complete'),
        path('listaruser/',listarUsuarios,name='listar'),
        path('eliminaruser/<int:id>',eliminarUsuario,name='eliminarUsuario'),
        path('agregargenero/', agregarGenero,name='agregargenero'),
        path('listargenero/',listarGeneros,name='listargenero'),
        path('modificargenero/<int:id>', modificarGenero,name='modificargenero'),
        path('eliminargenero/<int:id>', eliminarGenero,name='eliminargenero')
]