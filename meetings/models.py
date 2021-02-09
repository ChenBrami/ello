from django.db import models

# Create your models here.

class Meeting(models.Model):
    title = models.TextField()
    description = models.TextField()
    #date
    #time
    participants = models.TextField()
    location = models.TextField()