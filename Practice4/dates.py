#1 Write a Python program to subtract five days from current date.
import datetime
x = datetime.datetime.now()

a = x - datetime.timedelta(days=5)  #day-5

print(a)

#2 Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

#3 Write a Python program to drop microseconds from datetime.
import datetime
x = datetime.datetime.now()
m = x.replace(microsecond=0)
print(m)

#4 Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2025, 2, 10, 12, 0, 0)
date2 = datetime(2025, 2, 15, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print("Difference in seconds:", seconds)
