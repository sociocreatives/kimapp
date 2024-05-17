from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CategoryUganda
from .models import Colleges

def home(request):
    categories = CategoryUganda.objects.all()
    return render(request, 'index.html', {'categories': categories})

def about(request):
    return render(request, 'about.html', {})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        category_name = CategoryUganda.objects.filter(name__contains=searched)
        return render(request, 'search_results.html', {'searched':searched, category_name:category_name})
    else:
        return render(request, 'search_results.html', {})


