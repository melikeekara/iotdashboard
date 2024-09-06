from django.core.management.base import BaseCommand  # Importing BaseCommand class from django.core.management.base.
from device_monitor.models import Device  # Importing the Device model from device_monitor app.
import time  # Importing the time module.

class Command(BaseCommand):  # Defining a custom management command named Command, derived from BaseCommand.
    help = 'Monitors the status of IoT devices'  # Help text for the management command.

    def handle(self, *args, **options):  # Defining the handle method to execute the command.
        print("Starting device monitoring...")  # Displaying a message indicating the start of device monitoring.
        try:  # Handling KeyboardInterrupt to stop the infinite loop gracefully.
            while True:  # Running indefinitely.
                devices = Device.objects.all()  # Retrieving all Device instances from the database.
                print(f"Time: {time.strftime('%X')}")  # Printing the current time.
                for device in devices:  # Iterating over each device.
                    # Printing the status of each device including device ID, connection status, operational status, temperature, and last seen time.
                    print(f"Device ID: {device.device_id}, Status: {'Connected' if device.is_connected else 'Disconnected'}, Operational Status: {'Working' if device.operational_status else 'Not Working'}, Temperature: {device.temperature}, Last Seen: {device.last_seen} ")
                time.sleep(1)  # Waiting for 1 second before refreshing data.
                print("-" * 40)  # Printing a separator line.
        except KeyboardInterrupt:  # Handling KeyboardInterrupt when the user interrupts the command.
            print("Monitoring stopped.")  # Displaying a message indicating the monitoring is stopped.
