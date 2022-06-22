from django.db import models

# Create your models here.


class Driver(models.Model):
    username = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    vehicle_no = models.CharField(max_length=255, blank=False)
    ph_no = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=255, blank=False)
    is_registered = models.BooleanField(default=False)
    driver_liscence_pic = models.ImageField(
        upload_to="driverLiscence", blank=False)
    police_record = models.ImageField(upload_to="policeRecord", blank=False)
    available_seats = models.IntegerField()
    pickup_Location = models.CharField(max_length=255, blank=False)
    drop_Location = models.CharField(max_length=255, blank=False)
    is_airConditioned = models.BooleanField(default=False)
