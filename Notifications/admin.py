from django.contrib import admin

from .models import Notify

# Register your models here.


@admin.register(Notify)
class NotifyAdmin(admin.ModelAdmin):
    list_display = ['username', 'expotoken']
