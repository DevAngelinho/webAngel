from django.shortcuts import render, HttpResponse
from .models import Usuario

def home(request):
    def index(request):
        return render(request, 'index.html')

    return index(request)