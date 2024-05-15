from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category
from .models import Profile, Legal, WhyChoose
from .models import Tvets

def home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def about(request):
    return render(request, 'about.html', {})

def search_results(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        category_name = Category.objects.filter(name__contains=searched)
        return render(request, 'search_results.html', {'searched':searched, category_name:category_name})
    else:
        return render(request, 'search_results.html', {})


@login_required(login_url='/admin')
def profile(request):
    main_user = request.user
    user_profile = Profile.objects.filter(current_user=main_user)
    return render(request, 'profile.html', {'user_profile': user_profile})

def logout_view(request):
    logout(request)
    return redirect('home')

def legal(request):
    legal = Legal.objects.all()
    return render(request, 'legal.html', {'legal': legal})

def why_choose_us(request):
    whyus = WhyChoose.objects.all()
    return render(request, 'whychoose.html', {'whyus': whyus})

def how_it_works(request):
    whyus = WhyChoose.objects.all()
    return render(request, 'how_it_works.html', {'whyus': whyus})

