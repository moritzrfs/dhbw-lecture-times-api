from bs4 import BeautifulSoup
import requests
from .split_time import split_time, extract_date
from datetime import datetime, date, time
from .encoding import encode_to_utf8
from .lecture import Lecture

class Scraper:
    def __init__(self, url: str):
        self.url = url

    def get_soup(self):
        html = requests.get(self.url).text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def get_data(self):
        data = self.get_soup()
        days = data.find('div', {'class': 'ui-grid-e'})
        return days

    def lectures_json(self):
        lectures = self.get_lectures()
        lectures_json = []
        for lecture in lectures:
            lecture_json = {
                "name": lecture.name,
                "date": lecture.date.strftime("%d.%m.%Y"),
                "start_time": lecture.start_time.strftime("%H:%M"),
                "end_time": lecture.end_time.strftime("%H:%M"),
                "room": lecture.room,
                "info": lecture.info
            }
            lectures_json.append(lecture_json)
        return lectures_json

    def get_lectures(self) -> list[Lecture]:
        """
        Returns a a list ob lectures with type Lecture
        """
        lectures = []
        days = self.get_data()
        for day in days:
            ul = day.find('ul')
            try:
                lis = ul.find_all('li')
            except AttributeError:
                continue
            lecture_date = lis[0].text
            lecture_date = extract_date(lecture_date)
            for li in lis[1:]:
                try:
                    lecture_cal_time = li.find('div', {'class': 'cal-time'}).text
                    lecture_cal_title = encode_to_utf8(li.find('div', {'class': 'cal-title'}).text)
                    lecture_cal_room = li.find('div', {'class': 'cal-res'})
                    lecture_cal_text = li.find('div', {'class': 'cal-text'})
                except AttributeError:
                    continue

                if lecture_cal_text:
                    lecture_cal_text = encode_to_utf8(lecture_cal_text.text)
                else:
                    lecture_cal_text = None
                
                if lecture_cal_room:
                    lecture_cal_room = encode_to_utf8(lecture_cal_room.text)
                else:
                    lecture_cal_room = None
                
                start_time, end_time = split_time(lecture_cal_time)
                lecture = Lecture(lecture_cal_title, lecture_date, start_time, end_time, lecture_cal_room, lecture_cal_text)
                lectures.append(lecture)
    
        return lectures
