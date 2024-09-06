from django.db import models  # Importing the models module from Django.

class Device(models.Model):  # Defining a model named Device, derived from models.Model.
    device_id = models.CharField(max_length=100, unique=True)  # Creating a unique character field named device_id.
    is_connected = models.BooleanField(default=False)  # Creating a Boolean field named is_connected with a default value of False.
    last_seen = models.DateTimeField(auto_now=True)  # Creating a DateTime field named last_seen that automatically updates to the current time.
    temperature = models.CharField(max_length=100, null=True, blank=True)  # Creating an optional character field named temperature.
    operational_status = models.BooleanField(default=False)  # Creating a Boolean field named operational_status with a default value of False.
    humidity = models.CharField(max_length=100, null=True, blank=True)  # Creating an optional character field named humidity.

    def __str__(self):  # Defining a special method to determine the string representation of the model.
        status = 'Connected' if self.is_connected else 'Disconnected'  # Checking if the device is connected or disconnected.
        return f"{self.device_id} - {status}, Temp: {self.temperature}, Operational: {'Yes' if self.operational_status else 'No'}, Humidity: {self.humidity}"
        # Creating the string representation of the model, including device ID, connection status, temperature, operational status, and humidity.
