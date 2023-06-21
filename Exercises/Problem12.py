# 12. Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.

#Module to use calendar
import calendar

#Setting up variable for curr year/month
curr_year = 2023
curr_month = 6

print(calendar.month(curr_year, curr_month))
