from django.db import models

# Create your models here.

class Meeting(models.Model):
    title        = models.CharField(max_length=120, default='My New Meeting')
    description  = models.CharField(max_length=500, blank=True, null=True)
    participants = models.CharField(max_length=500, blank=True, null=True)
    location     = models.CharField(max_length=500, blank=True, null=True)
    # date
    # date
    # time
