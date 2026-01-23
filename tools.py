# tools.py

from datetime import datetime

def get_current_date_day():
    now = datetime.now()
    return now.strftime("Today is %A, %B %d, %Y.")

def get_current_time():
    now = datetime.now()
    return now.strftime("The current time is %I:%M %p.")
