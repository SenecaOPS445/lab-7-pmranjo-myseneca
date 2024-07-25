#!/usr/bin/env python3
# Student ID: pranjo
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:    # When seconds reach 60 a minute will be added while seconds go back to 0 after subtracting 60.
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:    # When minutes reach 60 a hour will be added while minutes go back to 0 after subtracting 60.
        sum.minute -= 60
        sum.hour += 1

    if sum.hour >= 24:      # Once hour reaches 24 it is resets back to 0.
        sum.hour -= 24

    return sum

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):

    time.second += seconds

    while time.second < 0:      # Once seconds is lower than 0 subtract 1 from minute and add 60 to seconds. Used to countdown.
        time.second += 60
        time.minute -= 1

    while time.minute < 0:      # Once minute is lower than 0 subtract 1 from hour and add 60 to minute. Used to countdown.
        time.minute += 60
        time.hour -= 1

    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1
        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1
    return None

#!/usr/bin/env python3
# Student ID: pranjo
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def time_to_sec(time):
    '''convert a time object to a single integer representing the number of seconds from mid-night'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):   
    '''convert a given number of seconds to a time object in hour,minute,second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    total_seconds %= 86400  # Handles when it exceeds 24 hours, 86400 is the number of seconds in an hour.
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 86400  # Handles if it exceeds 24 hours or is negative, 86400 is the number of seconds in an hour.
    return sec_to_time(total_seconds)