from django.shortcuts import render
from .models import Producto

def home(request):
    return index(request)

def interfaz(request):
    return render(request, 'interfaz.html')

def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)