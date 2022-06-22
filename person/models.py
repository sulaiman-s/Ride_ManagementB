from django.db import models


# Create your models here.
class PersonDriver(models.Model):
    driver_name = models.CharField(max_length=255, blank=False)
    person_name = models.CharField(max_length=255, blank=False)
    seats_booked = models.CharField(max_length=255, blank=False)
    message = models.CharField(max_length=255, blank=True)
    person_address = models.CharField(max_length=255, blank=False)
    person_pickup_Time = models.CharField(max_length=255, blank=False)

    driver_location = models.CharField(
        max_length=255, blank=True, default="32.4945,74.5229")
    person_location = models.CharField(
        max_length=255, blank=True, default="32.4945,74.5229")
