from django.contrib import admin
from .models import Driver


# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'email', 'driver_liscence_pic', 'is_registered', 'available_seats',
                    'pickup_Location', 'drop_Location', 'is_airConditioned']
