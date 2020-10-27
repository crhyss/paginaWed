from django.urls import path
from .views import paginaprincipal, listarProducto, modificarProducto, agregarProducto, eliminarProducto,administracion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', paginaprincipal,name="loby"),
    path('listar/', listarProducto, name="listar"),
    path('agregar/', agregarProducto, name='agregar'),
    path('modificar/<int:id_producto>', modificarProducto, name='modificar'),
    path('eliminar/<int:id_producto>', eliminarProducto, name='eliminar'),
    path('administracion/',administracion, name='admin')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
    )
