from django.db import models


class Location(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
