from fastapi import FastAPI
from scraper import Scraper
app = FastAPI()

@app.get("/lectures&gid={gid}&uid={uid}")
def get_lectures_week(gid: str, uid: str):
    """
    Returns a json object with all lectures of the week
    """
    print(gid, uid)
    scraper = Scraper(f"https://vorlesungsplan.dhbw-mannheim.de/index.php?action=view&gid={gid}&uid={uid}")
    json_lectures = scraper.lectures_json()
    return json_lectures

@app.get("/lectures&gid={gid}&uid={uid}&view=month")
def get_lectures_month(gid: str, uid: str):
    """
    Returns a json object with all lectures of the month
    """
    print(gid, uid)
    scraper = Scraper(f"https://vorlesungsplan.dhbw-mannheim.de/index.php?action=view&gid={gid}&uid={uid}&view=month")
    json_lectures = scraper.lectures_json()
    return json_lectures
