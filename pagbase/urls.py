from django.urls import path
from .views import paginaprincipal,datos,cuerpo
urlpatterns = [
    path('',paginaprincipal),
    path('loby/',datos, name="loby"),
    path('cuerpo/',cuerpo, name='cuerpo')
]
