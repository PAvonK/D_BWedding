from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')

def story(request):
    return render(request, 'homepage/story.html')

def gallery(request):
    return render(request, 'homepage/gallery.html')

def accommodation(request):
    return render(request, 'homepage/accommodation.html')

def contact(request):
    return render(request, 'homepage/contact.html')

def test(request):
    return render(request, 'homepage/test.html')