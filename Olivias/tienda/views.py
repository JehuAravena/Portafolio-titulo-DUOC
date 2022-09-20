from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def inicio(request):
    productos = producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/inicio.html', context)

def nosotros(request):
    return render(request, 'tienda/nosotros.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def tienda(request):
    productos = producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/tienda.html', context)

def login(request):
    return render(request, 'tienda/login.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

def venta(request):
    return render(request, 'tienda/venta.html')


    
