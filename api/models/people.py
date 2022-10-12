from os import name
from django.db import models

class People(models.Model):
    email = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=8) #range 18-25, 26-33, 34-40, 40+
    