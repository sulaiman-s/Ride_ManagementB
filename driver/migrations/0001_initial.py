# Generated by Django 4.0.5 on 2022-06-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('is_registered', models.BooleanField(default=False)),
                ('driver_liscence_pic', models.ImageField(blank=True, upload_to='driverLiscence')),
                ('available_seats', models.IntegerField()),
                ('pickup_Location', models.CharField(max_length=255)),
                ('drop_Location', models.CharField(max_length=255)),
            ],
        ),
    ]
