from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('tienda/', views.tienda, name='tienda'),
    path('login/', views.login, name='login'),
    path('carrito/', views.carrito, name='carrito'),
]