from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Pedidos)
admin.site.register(ProdPedido)
admin.site.register(DirDespacho)

