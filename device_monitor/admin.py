from django.contrib import admin  # Importing the admin module from Django.
from .models import Device  # Importing the Device model from the current package.

@admin.register(Device)  # Registering the Device model with the admin site.
class DeviceAdmin(admin.ModelAdmin):  # Defining a custom admin class for the Device model.
    list_display = ['device_id', 'is_connected', 'last_seen', 'temperature', 'operational_status', 'humidity']
    # Defining the fields to be displayed in the admin list view for Device instances.
