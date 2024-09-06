from django.apps import AppConfig  # Importing the AppConfig class from django.apps module.

class DeviceMonitorConfig(AppConfig):  # Defining a custom AppConfig class named DeviceMonitorConfig.
    default_auto_field = "django.db.models.BigAutoField"  # Setting the default_auto_field attribute to use BigAutoField for automatic primary keys.
    name = "device_monitor"  # Setting the name attribute to "device_monitor" to specify the application's name.
