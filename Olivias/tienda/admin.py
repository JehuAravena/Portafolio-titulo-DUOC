from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(pedido)
admin.site.register(prod_pedido)
admin.site.register(dir_despacho)

