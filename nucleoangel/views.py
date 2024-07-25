from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def interfaz(request):
    return render(request, 'interfaz.html')

def index(request):
    return render(request, 'index.html')

