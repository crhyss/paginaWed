from django.urls import path
from .views import iniciarSesion,registro,salir,perfil
urlpatterns = [
    path('login/',iniciarSesion, name='iniciarSesion'),
    path('registro/',registro, name='registro'),
    path('salir/',salir, name='salir'),
    path('perfil/',perfil, name='peril')
]