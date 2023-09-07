"""
Print the calendar of a given month and year
"""
import calendar
year = int(input("Enter the Year : "))
month = int(input("Enter the Month : "))
cal = calendar.month(year, month, w=0, l=0)
print(cal)