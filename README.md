﻿# iotdashboard
 Dashboard with Real-Time Monitoring

 This project aims to develop a real-time monitoring system for IoT devices using Django, a
high-level Python web framework. Real-time monitoring is a method used to monitor the
instantaneous status of IoT devices and make the necessary interventions in a timely manner.
The system integrates real-time monitoring capabilities into a control panel to provide instant
information about the status of IoT devices. The control panel visualizes measurements such as
device connectivity, sensor readings, and operational status using data streaming and
visualization techniques.
The development process includes the following steps:
• Firstly, a new Django project named "iot_dashboard" is created, followed by initiating a
Django application named "device_monitor" within the project directory.
• Database models are defined to store information about IoT devices, including device
ID, connection status, last seen timestamp, temperature, and humidity.
The Django admin interface is configured for easy management of device data, and database
migrations are performed to update the database schema according to the defined models.
Custom management commands are created for periodic updating of device data and
monitoring device data in the terminal.
An executable command file named "run_commands.bat" is developed to automate Django
commands. The entire setup is verified by adding device data through the Django admin panel
and observing updates and monitoring outputs in the terminal.
In conclusion, this project provides an abstract real-time monitoring and management system
for IoT devices with the use of Django.

![image](https://github.com/user-attachments/assets/dfe911f1-73dc-40e6-8efd-8902ea940aa4)

