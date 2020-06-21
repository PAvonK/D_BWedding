from django.urls import path
from . import views

urlpatterns = [
    path('', views.rsvp),
    path('response/', views.response_detail),
]