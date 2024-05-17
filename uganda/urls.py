from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search_results/', views.search_results, name='search_results'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_views'),
]