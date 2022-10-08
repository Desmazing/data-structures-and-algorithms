"""
  Working with th datetime module is an important Pythonista skill
"""

from datetime import datetime
from datetime import time
from datetime import date

day1 = input("Enter 1st date: ")
day2 = input("Enter 2nd date: ")

date_format = "%d/%m/%Y"

d1 = datetime.strptime(day1, date_format)
d2 = datetime.strptime(day2, date_format)
diff = d2-d1

print(diff.days)

# the following code is for practice
today = date.today()
print("Today's date is", today)
print("The month is", today.month) 
# the month is an attribute of the date object
print("The day is", today.day)
# the day is an attribute of the date object 
# we can also do the same for year
print("The day is", today.year)
# the year is an attribute of the date object 

t1 = input("Enter time 1: ")
t2 = input("Enter time 2: ")

time_format = "%H/%M/%S"

tim1 = datetime.strptime(t1, time_format) # this method creates a time object from string
tim2 = datetime.strptime(t2, time_format)

td = tim2 - tim1

print("Hour difference is", (td.seconds/3600), "hours") 

# worth noting that timedelta has no hour attribute. just days and seconds hence conversions
# td.hours would thus not work
