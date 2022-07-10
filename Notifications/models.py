from django.db import models

# Create your models here.


class Notify(models.Model):
    username = models.CharField(max_length=255)
    expotoken = models.CharField(max_length=300)
