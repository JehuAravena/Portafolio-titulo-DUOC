from django.shortcuts import render
from django.http import JsonResponse
from numpy import product
import datetime
import json

# se importan los modelos de la base de datos
from .models import *
from . utils import *

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
    productos = Productos.objects.all()
    # se crea un diccionario con los productos
    context = {'productos': productos}
    # se renderiza la pagina tienda.html con los productos
    return render(request, 'tienda/tienda.html', context)


def login(request):
    # se renderiza la pagina login.html
    return render(request, 'tienda/login.html')


def carrito(request):
    data = cartData(request)
    items = data['items']
    pedido = data['pedido']
    itemsCarrito = data['itemsCarrito']
    
    context = {'items': items, 'pedido': pedido, 'itemsCarrito': itemsCarrito}
    
    # se renderiza la pagina carrito.html con los items y el pedido
    return render(request, 'tienda/carrito.html', context)


def venta(request):

    data = cartData(request)
    items = data['items']
    pedido = data['pedido']
    itemsCarrito = data['itemsCarrito']

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
    # se obtiene el id de la transaccion
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)  # se obtiene la informacion del body

    if request.user.is_authenticated:  # si el usuario esta autenticado
        cliente = request.user.clientes  # se obtiene el cliente
        pedido, creado = Pedidos.objects.get_or_create(  # se obtiene el pedido, si no existe se crea
            cliente=cliente, estado=False)  # el pedido se crea con el cliente y el estado en False

    else:  # si el usuario no esta autenticado
        cliente, pedido = guestOrder(request, data)  # se crea un pedido para el usuario invitado

    total = float(data['form']['total'])
    # se asigna el id de la transaccion al pedido
    pedido.transaction_id = transaction_id

    if total == pedido.get_carrito_total:  # si el total del pedido es igual al total del carrito
        pedido.estado = True  # el pedido se marca como completado
    pedido.save()  # se guarda el pedido

    if pedido.estado:  # si el pedido esta completado
        # se crea la direccion de envio
        DirDespacho.objects.create(
            cliente=cliente,
            pedido=pedido,
            direccion=data['formEnvio']['address'],
            ciudad=data['formEnvio']['city'],
            region=data['formEnvio']['state'],
        )

    return JsonResponse('Pago completado...', safe=False)
