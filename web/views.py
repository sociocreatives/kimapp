from django.shortcuts import render
from .models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def about(request):
    return render(request, 'about.html', {})