from datetime import date, time

class Lecture:
    """
    A class to represent a lecture
    """
    def __init__(self, name: str, date: date , start_time: time, end_time: time, room: str, info: str = None):
        (self.name) = name
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.room = room
        self.info = info


    def __str__(self):
        return f"{self.name} {self.start_time} {self.end_time} {self.room}"
