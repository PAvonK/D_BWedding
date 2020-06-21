from django import forms
from . import models 

class Rsvp_Form(forms.ModelForm):
    
    class Meta:
        model = models.rsvp
        fields = [
            'full_name',
            'email',
            'please_check_if_you_are_able_to_attend',
            'number_attending',
            'message_for_the_happy_couple'
        ]