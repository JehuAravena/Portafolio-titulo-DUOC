from django.shortcuts import render
from .models import *

# Create your views here.
def inicio(request):
    productos = Productos.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/inicio.html', context)

def nosotros(request):
    return render(request, 'tienda/nosotros.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')

def tienda(request):
    productos = Productos.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/tienda.html', context)

def login(request):
    return render(request, 'tienda/login.html')

def carrito(request):
    if request.user.is_authenticated: # si el usuario esta autenticado
        cliente = request.user.clientes
        pedido, creado = Pedidos.objects.get_or_create(cliente=cliente, estado=False)
        items = pedido.prodpedido_set.all()
    else: 
        items = [] 
        pedido = {'get_carrito_total': 0, 'get_carrito_items': 0} # si no hay usuario, no hay pedido

    context = {'items': items, 'pedido': pedido}
    return render(request, 'tienda/carrito.html', context)

def venta(request):
    if request.user.is_authenticated: # si el usuario esta autenticado
        cliente = request.user.clientes
        pedido, creado = Pedidos.objects.get_or_create(cliente=cliente, estado=False)
        items = pedido.prodpedido_set.all()
    else:
        items = []
        pedido = {'get_carrito_total': 0, 'get_carrito_items': 0}

    context = {'items': items, 'pedido': pedido}
    return render(request, 'tienda/venta.html', context)


    
