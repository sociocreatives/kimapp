from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('legal/', views.legal, name='legal'),
    path('why-choose-us/', views.why_choose_us, name='why-choose-us'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('search_results/', views.search_results, name='search_results'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_views'),
]

