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
from django.http import HttpResponse  # ← ADD THIS
from django.contrib.auth.models import User  # ← ADD THIS
import os  # ← ADD THIS

# ADD THIS FUNCTION
def create_superuser(request):
    # ... (the function code from above)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),
    
    # ADD THIS LINE
    path('create-admin-user/', create_superuser, name='create_superuser'),
]
