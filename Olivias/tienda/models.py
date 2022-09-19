import imp
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class cliente(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nombre


class producto(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=500, null=True)
    imagen = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class pedido(models.Model):
    cliente = models.ForeignKey(cliente, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(
        producto, null=True, on_delete=models.SET_NULL)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.producto.nombre

class prod_pedido(models.Model):
    pedido = models.ForeignKey(pedido, null=True, on_delete=models.SET_NULL)
    producto = models.ForeignKey(producto, null=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.producto.nombre

class dir_despacho(models.Model):
    cliente = models.ForeignKey(cliente, null=True, on_delete=models.SET_NULL)
    pedido = models.ForeignKey(pedido, null=True, on_delete=models.SET_NULL)
    direccion = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.direccion