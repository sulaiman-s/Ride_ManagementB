# Generated by Django 4.0.5 on 2022-06-20 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0004_driver_police_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='is_airConditioned',
            field=models.BooleanField(default=False),
        ),
    ]
