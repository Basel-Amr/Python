# -*- coding: utf-8 -*-
"""
Quick Task (2)
Write Python Code that handle the following login system
UserName    Password
Ahmed       1394
Ali         6078
Amr         9345
If the data entered is correct, the system shall print welcome message, if not the 
system will print incorrect entery
"""

import psutil

#get cpu percentage
print("CPU Usage", psutil.cpu_percent())

#get memory usage statistics
memory = psutil.virtual_memory()
print("Total Memory : ",memory.total/1000000000, "G")
print("Available Memory : ",memory.available/1000000000, "G")
print("Used Memory : ",memory.used/1000000000, "G")
print("Memory used perecntage: ",memory.percent)

#get disk usage Statistics
disk = psutil.disk_usage('/')
print("Total Disk Space : ",disk.total/1000000000, "G")
print("used Disk Space : ",disk.used/1000000000, "G")
print("free Disk free : ",disk.free/1000000000, "G")
print("Disk Usage Percentage: ",disk.percent)