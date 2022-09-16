from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'tienda/inicio.html')

def nosotros(request):
    return render(request, 'tienda/nosotros.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def tienda(request):
    return render(request, 'tienda/tienda.html')

def login(request):
    return render(request, 'tienda/login.html')

def carrito(request):
    return render(request, 'tienda/carrito.html')

def venta(request):
    return render(request, 'tienda/venta.html')


    
