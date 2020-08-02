from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def story(request):
    return render(request, 'homepage/story.html')

def gallery(request):
    return render(request, 'homepage/gallery.html')

def registry(request):
    return render(request, 'homepage/registry.html')

@login_required
def location(request):
    return render(request, 'homepage/location.html')

@login_required
def contact(request):
    return render(request, 'homepage/contact.html')

@login_required
def test(request):
    return render(request, 'homepage/test.html')

