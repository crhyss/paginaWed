from django.urls import path
from .views import iniciarSesion,registro,salir,perfil,verificacion
urlpatterns = [
    path('login/',iniciarSesion, name='iniciarSesion'),
    path('registro/',registro, name='registro'),
    path('salir/',salir, name='salir'),
    path('perfil/',perfil, name='peril'),
    path('activacion/<uidb64>/<token>',verificacion.as_view(), name='activacion')
]