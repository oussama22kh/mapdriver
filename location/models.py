from django.db import models


class Location(models.Model):
    id = models.TextField(max_length=255,primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
