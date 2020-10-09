from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.

def paginaprincipal(request):
    return render(
        request,
        'pagbase/ingreso.html'
    )
def datos(request):
    return render(
        request,
        'pagbase/registro.html'
    )
def cuerpo(request):
    return render(
        request,
        'pagbase/cuerpo.html'
    )