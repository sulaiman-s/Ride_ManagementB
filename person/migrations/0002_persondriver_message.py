# Generated by Django 4.0.5 on 2022-06-14 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persondriver',
            name='message',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
