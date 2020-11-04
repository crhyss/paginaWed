from django.urls import path
from .views import *


app_name = "cart"
urlpatterns = [
    path('agregarproducto/<int:producto_id>/',agregarProducto,name="agregarproducto"),
    path('eliminarproducto/<int:producto_id>/',eliminarProducto,name="eliminarproducto"),
    path('decrementarproducto/<int:producto_id>/',decrementarProducto,name="decrementarproducto"),
    path('limpiarcarro/',limpiarCarrito,name="limpiarcarrito"),
]