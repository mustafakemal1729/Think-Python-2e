# Exercise 5-1.

"""

The time module provides a function, also named time, that returns the current
Greenwich Mean Time in “the epoch”, which is an arbitrary time used as a reference point.
On UNIX systems, the epoch is 1 January 1970.

        >>> import time
        >>> time.time()
        1437746094.5735958

Write a script that reads the current time and converts it to a time of day in hours,
minutes, and seconds, plus the number of days since the epoch.
"""

# time.time() returns the number of seconds since EPOCH
import time

def current_time():
    
    epoch = int(time.time())

    days_since_epoch = epoch / (60 * 60 * 24)
    hour = days_since_epoch % int(days_since_epoch) * 24
    minute  = hour % int(hour) * 60
    second  = minute % int(minute) * 60
    
    print(f"Days: {int(days_since_epoch)} \nTime: {int(hour)}:{int(minute)}:{int(second)}")


current_time()