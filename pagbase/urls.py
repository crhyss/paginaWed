from django.urls import path
from .views import paginaprincipal,listarProducto,modificarProducto,agregarProducto,eliminarProducto
urlpatterns = [
    path('',paginaprincipal, name="loby"),
    path('listar/',listarProducto, name="listar"),
    path('agregar/',agregarProducto, name='agregar'),
    path('modificar/<int:id_producto>',modificarProducto, name='modificar'),
    path('eliminar/<int:id_producto>',eliminarProducto, name='eliminar')
]
