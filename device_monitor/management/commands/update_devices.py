import random  # Importing the random module to generate random data.
from django.core.management.base import BaseCommand  # Importing BaseCommand class from django.core.management.base.
from device_monitor.models import Device  # Importing the Device model from device_monitor app.
from django.utils import timezone  # Importing timezone module from django.utils.
import time  # Importing the time module.

class Command(BaseCommand):  # Defining a custom management command named Command, derived from BaseCommand.
    help = 'Updates device data periodically'  # Help text for the management command.

    def handle(self, *args, **options):  # Defining the handle method to execute the command.
        
        try:  # Handling KeyboardInterrupt to stop the infinite loop gracefully.
            while True:  # Running indefinitely.
                self.update_devices()  # Calling the update_devices method to update device data.
                time.sleep(2)  # Waiting for 2 seconds before the next update.
        except KeyboardInterrupt:  # Handling KeyboardInterrupt when the user interrupts the command.
            self.stdout.write("Stopping device data updates...")  # Displaying a message indicating the command is stopped.

    def update_devices(self):  # Defining a method to update device data.
        devices = Device.objects.all()  # Retrieving all Device instances from the database.
        for device in devices:  # Iterating over each device.
            device.is_connected = random.choice([True, False])  # Setting is_connected field randomly.
            device.temperature = f"{random.randint(18, 35)}°C"  # Generating a random temperature value.
            device.operational_status = random.choice([True, False])  # Setting operational_status field randomly.
            device.humidity = f"{random.randint(40, 60)}%"  # Generating a random humidity value.
            device.last_seen = timezone.now()  # Updating the last_seen field with the current time.
            device.save()  # Saving the changes to the device instance in the database.
