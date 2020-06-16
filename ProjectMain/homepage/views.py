from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def story(request):
    return render(request, 'homepage/story.html')

def gallery(request):
    return render(request, 'homepage/gallery.html')

@login_required
def location(request):
    return render(request, 'homepage/location.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def test(request):
    return render(request, 'homepage/test.html')

@login_required
def rsvp(request):
    return render(request, 'homepage/rsvp.html')

