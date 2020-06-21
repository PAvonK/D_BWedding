from django import forms
from . import models 

class Rsvp_Form(forms.ModelForm):
    
    class Meta:
        model = models.rsvp
        fields = [
            'last_name',
            'first_name',
            'email',
            'attending',
            'number_attending',
            'message_for_the_happy_couple'
        ]