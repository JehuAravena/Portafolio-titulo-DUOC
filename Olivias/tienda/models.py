from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Clientes(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=500, null=True)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Pedidos(models.Model):
    cliente = models.ForeignKey(Clientes, null=True, on_delete=models.SET_NULL)
    # Producto = models.ForeignKey(
    #     Producto, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.BooleanField(default=False) # completado o no completado
    id_transaccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_carrito_total(self): # total de la compra
        items = self.prodpedido_set.all()
        total = sum([item.get_total for item in items])
        return total

    @property
    def get_carrito_items(self): # cantidad de productos
        items = self.prodpedido_set.all()
        total = sum([item.cantidad for item in items])
        return total

class ProdPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(Productos, null=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total

class DirDespacho(models.Model):
    cliente = models.ForeignKey(Clientes, null=True, on_delete=models.SET_NULL)
    pedido = models.ForeignKey(Pedidos, null=True, on_delete=models.SET_NULL)
    direccion = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.direccion