#print one month calander
import calendar
# Enter the year and month you want to print the calendar for
year = 2003
month = 5
# Create a calendar object
cal = calendar.month(year, month)
# Print the calendar
print(cal)

#print whole year calander

import calendar
def print_calendar(year):
  print(calendar.prcal(year))
year = 2003
print_calendar(year)

