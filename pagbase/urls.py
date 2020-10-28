from django.urls import path
from .views import paginaprincipal, listarProducto, modificarProducto, agregarProducto, eliminarProducto,administracion,moda
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', paginaprincipal,name="loby"),
    path('listar/', listarProducto, name="listar"),
    path('agregar/', agregarProducto, name='agregar'),
    path('modificar/<int:id_producto>', modificarProducto, name='modificar'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='eliminar'),
    path('administracion/',administracion, name='admin'),
    path('moda/',moda, name='moda')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )
