from django.shortcuts import render
from django.http import JsonResponse
import json

from numpy import product

# se importan los modelos de la base de datos
from .models import *

# Create your views here.


def inicio(request):
    # se obtienen todos los productos de la base de datos
    productos = Productos.objects.all()
    # se crea un diccionario con los productos
    context = {'productos': productos}
    # se renderiza la pagina inicio.html con los productos
    return render(request, 'tienda/inicio.html', context)


def nosotros(request):
    # se renderiza la pagina nosotros.html
    return render(request, 'tienda/nosotros.html')


def contacto(request):
    # se renderiza la pagina contacto.html
    return render(request, 'tienda/contacto.html')


def tienda(request):
    # se obtienen todos los productos de la base de datos
    productos = Productos.objects.all()
    # se crea un diccionario con los productos
    context = {'productos': productos}
    # se renderiza la pagina tienda.html con los productos
    return render(request, 'tienda/tienda.html', context)


def login(request):
    # se renderiza la pagina login.html
    return render(request, 'tienda/login.html')


def carrito(request):
    if request.user.is_authenticated:  # si el usuario esta autenticado
        cliente = request.user.clientes  # se obtiene el cliente
        pedido, creado = Pedidos.objects.get_or_create(  # se obtiene el pedido, si no existe se crea
            cliente=cliente, estado=False)  # el pedido se crea con el cliente y el estado en False
        items = pedido.prodpedido_set.all()  # se obtienen los items del pedido
        # se obtiene el numero de items del pedido
        itemsCarrito = pedido.get_carrito_items
    else:  # si el usuario no esta autenticado
        items = []  # se crea una lista vacia
        # se crea un diccionario con el total y el numero de items en 0
        pedido = {'get_carrito_total': 0, 'get_carrito_items': 0}
        # se obtiene el numero de items del pedido
        itemsCarrito = pedido['get_carrito_items']

    # se crea un diccionario con los items y el pedido
    productos = Productos.objects.all()
    # se renderiza la pagina carrito.html con los items y el pedido
    context = {'items': items, 'pedido': pedido,
               'productos': productos, 'itemsCarrito': itemsCarrito}
    # se renderiza la pagina carrito.html con los items y el pedido
    return render(request, 'tienda/carrito.html', context)


def venta(request):
    if request.user.is_authenticated:  # si el usuario esta autenticado
        cliente = request.user.clientes  # se obtiene el cliente
        pedido, creado = Pedidos.objects.get_or_create(  # se obtiene el pedido, si no existe se crea
            cliente=cliente, estado=False)  # el pedido se crea con el cliente y el estado en False
        items = pedido.prodpedido_set.all()  # se obtienen los items del pedido
    else:  # si el usuario no esta autenticado
        items = []  # se crea una lista vacia
        # se crea un diccionario con el total y el numero de items en 0
        pedido = {'get_carrito_total': 0, 'get_carrito_items': 0}

    # se crea un diccionario con los items y el pedido
    context = {'items': items, 'pedido': pedido}
    # se renderiza la pagina venta.html con los items y el pedido
    return render(request, 'tienda/venta.html', context)


def actualizarItem(request):
    data = json.loads(request.body)  # se obtiene la informacion del body
    productoId = data['productoId']  # se obtiene el id del producto
    accion = data['accion']  # se obtiene la accion

    print('Accion:', accion)  # se imprime la accion
    print('Producto:', productoId)  # se imprime el id del producto

    cliente = request.user.clientes  # se obtiene el cliente
    producto = Productos.objects.get(id=productoId)  # se obtiene el producto
    pedido, creado = Pedidos.objects.get_or_create(  # se obtiene el pedido, si no existe se crea
        cliente=cliente, estado=False)  # el pedido se crea con el cliente y el estado en False

    prodpedido, creado = ProdPedido.objects.get_or_create(  # se obtiene el item del pedido, si no existe se crea
        pedido=pedido, producto=producto)  # el item del pedido se crea con el pedido y el producto

    if accion == 'add':  # si la accion es agregar
        # se aumenta la cantidad del item en 1
        prodpedido.cantidad = (prodpedido.cantidad + 1)
    elif accion == 'remove':  # si la accion es remover
        # se disminuye la cantidad del item en 1
        prodpedido.cantidad = (prodpedido.cantidad - 1)

    prodpedido.save()  # se guarda el item del pedido

    if prodpedido.cantidad <= 0:  # si la cantidad del item es menor o igual a 0
        prodpedido.delete()  # se elimina el item del pedido

    # se retorna un mensaje de que el item fue agregado
    return JsonResponse('Se añadio al carrito', safe=False)


def procesarOrden(request):
    print('Data:', request.body)  # se imprime la informacion del body
    return JsonResponse('Orden procesada', safe=False)
