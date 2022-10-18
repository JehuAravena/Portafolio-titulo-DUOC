import json
from . models import *


def cookieCart(request):
    try:
        carrito = json.loads(request.COOKIES['carrito'])
    except:
        carrito = {}

    print('carrito:', carrito)
    items = []  # se crea una lista vacia
    # se crea un diccionario con el total y el numero de items en 0
    pedido = {'get_carrito_total': 0, 'get_carrito_items': 0}
    # se obtiene el numero de items del pedido
    itemsCarrito = pedido['get_carrito_items']

    for i in carrito:
        try:
            itemsCarrito += carrito[i]['cantidad']

            producto = Productos.objects.get(id=i)
            total = (producto.precio * carrito[i]['cantidad'])

            pedido['get_carrito_total'] += total
            pedido['get_carrito_items'] += carrito[i]['cantidad']

            item = {
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'imagen': producto.imagen,
                },
                'cantidad': carrito[i]['cantidad'],
                'get_total': total,
                }
            items.append(item)
        except:
            pass
    return {'items': items, 'pedido': pedido, 'itemsCarrito': itemsCarrito}


def cartData(request):
    if request.user.is_authenticated:  # si el usuario esta autenticado
        cliente = request.user.clientes  # se obtiene el cliente
        pedido, creado = Pedidos.objects.get_or_create(  # se obtiene el pedido, si no existe se crea
            cliente=cliente, estado=False)  # el pedido se crea con el cliente y el estado en False
        items = pedido.prodpedido_set.all()  # se obtienen los items del pedido
        # se obtiene el numero de items del pedido
        itemsCarrito = pedido.get_carrito_items
    else:  # si el usuario no esta autenticado
        # se obtiene la informacion del carrito
        cookieData = cookieCart(request)
        items = cookieData['items']  # se obtienen los items del carrito
        pedido = cookieData['pedido']  # se obtiene el pedido del carrito
        # se obtiene el numero de items del carrito
        itemsCarrito = cookieData['itemsCarrito']

    return {'items': items, 'pedido': pedido, 'itemsCarrito': itemsCarrito}


def guestOrder(request, data):
    print('Usuario no registrado')

    print('COOKIES:', request.COOKIES)
    nombre = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    cliente, creado = Clientes.objects.get_or_create(
        email=email,
    )
    cliente.nombre = nombre
    cliente.save()

    pedido = Pedidos.objects.create(
        cliente=cliente,
        estado=False,
    )

    for item in items:
        producto = Productos.objects.get(id=item['producto']['id'])

        prodPedido = ProdPedido.objects.create(
            producto=producto,
            pedido=pedido,
            cantidad=item['cantidad']
        )
    return cliente, pedido
