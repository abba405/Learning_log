"""Defines URL patterns for users"""

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'users'
urlpatterns = [
    # Custom logout that accepts GET requests - put this BEFORE the include
    path('logout/', LogoutView.as_view(), name='logout'),
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]