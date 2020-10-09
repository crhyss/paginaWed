from django.urls import path
from .views import paginaprincipal,datos,cuerpo
urlpatterns = [
    path('',paginaprincipal),
    path('loby/',datos),
    path('cuerpo/',cuerpo)
]
