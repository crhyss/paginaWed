from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.

def paginaprincipal(request):
    return hr("Pagina principal")