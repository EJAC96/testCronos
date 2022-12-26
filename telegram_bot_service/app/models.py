from django.db import models

# Create your models here.

class ABC(models.Model):
    name = models.CharField(max_length=20)
    monile = models.CharField(max_length=15, blank=False)