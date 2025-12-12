from django.urls import path
from . import views

urlpatterns = [
    path('<uuid:code>/', views.rsvp_view, name='rsvp'),
]
