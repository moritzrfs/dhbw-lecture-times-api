from datetime import datetime

def split_time(time_string):
    """
    Splits a time string into a tuple of two 
    datetime.time objects. The time string must
    be in the format of "HH:MM-HH:MM"
    (e.g. "08:15-09:45")
    """
    
    start_time, end_time = time_string.split("-")
    start_time = datetime.strptime(start_time, "%H:%M").time()
    end_time = datetime.strptime(end_time, "%H:%M").time()
    return start_time, end_time

def extract_date(date_string):
    """
    Extracts a datetime.date object from a date string.
    The dare string is in the format Day, DD.MM. It adds
    the current year to the date object.
    """
        
    date_string = date_string.split(", ")[1]
    date_string = date_string + f".{datetime.now().year}"
    date = datetime.strptime(date_string, "%d.%m.%Y").date()
    return date