from django.urls import path
from .views import paginaprincipal
urlpatterns = [
    path('',paginaprincipal)
    
]
