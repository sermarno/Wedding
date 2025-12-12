"""
URL configuration for wedWebsite project.
- decides what happens when someone visits a certain page 
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
