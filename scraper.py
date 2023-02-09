from bs4 import BeautifulSoup
import requests

class Lecture:
    def __init__(self, name, time, room):
        self.name = name
        self.time = time
        self.room = room

    def __str__(self):
        return f'{self.name} {self.time} {self.room}'


def get_soup(url):
    """Returns the soup of a url"""
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

data = get_soup('https://vorlesungsplan.dhbw-mannheim.de/index.php?action=view&gid=3067001&uid=8064001')
divs = data.find('div', {'class': 'ui-grid-e'})
lectures = []

for div in divs:
    ul = div.find('ul')
    lis = ul.find_all('li')
    lecture_date = lis[0].text


    for li in lis[1:]:
        lecture_cal_time = li.find('div', {'class': 'cal-time'})
        lecture_cal_title = li.find('div', {'class': 'cal-title'})
        lecture_cal_room = li.find('div', {'class': 'cal-res'})
        print(lecture_cal_time.text)

    

    _lecture = Lecture("Temp", lecture_date, "Temp")
    lectures.append(_lecture)

for lecture in lectures:
    print(lecture)