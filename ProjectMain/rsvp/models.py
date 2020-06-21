from django.db import models
from django.utils import timezone

class Rsvp(models.Model):
    lastname = models.CharField(max_length=100)
    firsname = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    email = models.EmailField(max_length=100)
    attending = models.TextChoices('No', 'Yes')
    number_guests = models.CharField(max_length=2)
    couple_message = models.TextField()





class Snippet(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.name
