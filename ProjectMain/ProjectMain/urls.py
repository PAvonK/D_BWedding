"""ProjectMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from homepage import views as homepage_views
from users import views as user_views
from rsvp import views as rsvp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    
    path('', include('homepage.urls')),
    path('story/', homepage_views.story, name='story'),
    path('gallery/', homepage_views.gallery, name='gallery'),
    path('registry/', homepage_views.registry, name='registry'),
    path('location/', homepage_views.location, name='location'),
    path('contact/', homepage_views.contact, name='contact'),
    path('test/', homepage_views.test, name='test'),
    
    path('rsvp/', rsvp_views.rsvpData, name='rsvp'),
    path('csv_export/', rsvp_views.csv_export, name='csv_export'),
    path('location/', rsvp_views.location, name='location'),
    # just for testing / examples - have to access by /rsvp1
    path('rsvp1/', rsvp_views.rsvp1, name='rsvp1'),
    # just for testing / examples - have to access by /accommodation
    path('accommodation/', rsvp_views.accommodation, name='accommodation'),
    # just for testing / examples - have to access by /elements
    path('elements/', rsvp_views.elements, name='elements'),
    
    path('profile/', user_views.profile, name='profile'),
]
