from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import forms

@login_required
def rsvp(request):
    if request.method == 'POST':
        form = forms.Rsvp_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            number_attending = form.cleaned_data['number_attending']
            message_for_the_happy_couple = form.cleaned_data['message_for_the_happy_couple']
            messages.success(request, f'Thank you {full_name} for your RSVP!!!')
            return redirect('location')
    
    else:
        form = forms.Rsvp_Form()
    return render(request, 'rsvp/rsvp.html', {'form': form})
