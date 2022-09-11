from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def tienda(request):
    return render(request, 'tienda/index.html')

def nosotros(request):
    return render(request, 'tienda/about-us.html')

def contacto(request):
    return render(request, 'tienda/contacts.html')

def tienda(request):
    return render(request, 'tienda/typography.html')