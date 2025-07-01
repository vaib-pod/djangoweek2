"""
URL configuration for core project.

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
from django.contrib import admin
from django.urls import path,include
from habits.views import *

from django.conf import settings
from django.contrib.auth.urls import views as auth_views


urlpatterns = [
    path('', habit_list, name='habit_list'),
    path('create/', habit_create, name='habit_create'),
    path('<int:habit_id>/delete/', habit_delete, name='habit_delete'),
    path('<int:habit_id>/edit/', habit_edit, name='habit_edit'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
  
]

