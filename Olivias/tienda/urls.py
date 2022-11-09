from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('tienda/', views.tienda, name='tienda'),
    path('login/', views.login, name='login'),
    path('carrito/', views.carrito, name='carrito'),
    path('venta/', views.venta, name='venta'),
    path('actualizar_item/', views.actualizarItem, name='actualizar_item'),
    path('procesar_orden/', views.procesarOrden, name='procesar_orden'),
    path('ingresado/', views.ingresado, name='ingresado'),
    path('producto/<str:slug>/<int:id>/', views.producto, name='producto'),
]