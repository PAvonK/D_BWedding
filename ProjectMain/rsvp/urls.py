from django.urls import path
from . import views

urlpatterns = [
    path('', views.rsvp),
    path('snippet', views.snippet_detail),
]