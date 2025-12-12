"""
URL configuration for wedWebsite project.
- decides what happens when someone visits a certain page 
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rsvp/', include('rsvp.urls')),
    path('', include('home.urls')),
]
