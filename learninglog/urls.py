"""
URL configuration for learninglog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# learninglog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.models import User
import os

def create_superuser(request):
    """Temporary view to create superuser"""
    try:
        if User.objects.filter(username='admin', is_superuser=True).exists():
            return HttpResponse("Superuser already exists!")
        
        User.objects.create_superuser('Abba', 'zakariyaibrahim3551@gmail.com', '07065743551Zaks@')
        return HttpResponse("Superuser created successfully!")
        
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),  # Make sure this matches your app name
    path('users/', include('users.urls')),   # If you have a users app
    
    # Temporary URL
    path('create-admin-user/', create_superuser),
]
