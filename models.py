from django.db import models


class Store(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    production_year = models.IntegerField()
    price = models.FloatField()
    transmission_mode = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    engine_capacity = models.CharField(max_length=255)
    full_wheelDrive = models.BooleanField()
    # image_url = models.CharField(max_length=2083)

# Create your models here.
