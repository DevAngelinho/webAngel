from django.shortcuts import render
from .models import Producto

def home(request):
    return index(request)

def interfaz(request):
    return render(request, 'interfaz.html')

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

