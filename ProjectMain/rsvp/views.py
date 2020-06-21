from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RsvpForm, SnippetForm


# Create your views here.

@login_required
def rsvp(request):
    
    if request.method == "POST":
        form = RsvpForm(request.POST)
        if form.is_valid():
            #form.save()
            name = form.cleaned_data.get['name']
            #name_last = form.cleaned_data['name_last']
            email = form.cleaned_data['email']
            messages.success(request, f'Thank you {name} for your RSVP!!!')
            return redirect('location')
            
            print(name)
            

    else:
        form = RsvpForm()
    return render(request, 'rsvp/rsvp.html', {'form': form})


def snippet_detail(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


    form = SnippetForm()
    return render(request, 'rsvp/rsvp.html', {'form': form})
