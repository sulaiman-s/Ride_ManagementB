# Generated by Django 4.0.5 on 2022-06-13 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_driver_ph_no_driver_vehicle_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='driver_liscence_pic',
            field=models.ImageField(upload_to='driverLiscence'),
        ),
    ]
