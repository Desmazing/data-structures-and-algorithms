# program to convert date to milliseconds
# could easily use time since epoch

from datetime import datetime

right_now = datetime.now()

print("Datetime is", right_now)

millisecond_time = datetime.now().timestamp() * 1000
print("Time in milliseconds is", millisecond_time)