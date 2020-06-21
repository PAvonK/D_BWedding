from django.db import models
from django.utils import timezone



class rsvp(models.Model):
    
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=75)
    attending = models.BooleanField()
    number_attending = models.IntegerField()
    message_for_the_happy_couple = models.TextField(max_length=500, blank=True)
