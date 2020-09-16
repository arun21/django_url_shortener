from django.db import models
from django import forms


# Create your models here.

class short_urls(models.Model):
    short_url = models.CharField(max_length=20)
    long_url = models.URLField('Enter URL ', unique=True)
    comment = models.CharField(blank=True, max_length=100)
