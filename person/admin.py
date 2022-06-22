from django.contrib import admin
from .models import PersonDriver
# Register your models here.


@admin.register(PersonDriver)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['driver_name', 'person_name',
                    'seats_booked', 'driver_location', 'person_location']
