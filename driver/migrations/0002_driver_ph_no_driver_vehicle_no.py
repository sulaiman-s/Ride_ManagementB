# Generated by Django 4.0.5 on 2022-06-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='ph_no',
            field=models.CharField(default='ok', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='vehicle_no',
            field=models.CharField(default='ok', max_length=255),
            preserve_default=False,
        ),
    ]