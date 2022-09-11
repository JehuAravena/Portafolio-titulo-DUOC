from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('tienda/', views.tienda, name='tienda'),
]

