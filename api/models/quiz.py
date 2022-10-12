from email.policy import default
from django.db import models
from .people import People
from .company import Company

class Quiz(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    favorite_social_network = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)
    time_facebook = models.PositiveSmallIntegerField()
    time_whatsapp = models.PositiveSmallIntegerField()
    time_twitter = models.PositiveSmallIntegerField()
    time_instagram = models.PositiveSmallIntegerField()
    time_tiktok = models.PositiveSmallIntegerField()