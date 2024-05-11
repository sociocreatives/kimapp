from django.shortcuts import render
from .models import Category

def Home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})