import sqlite3
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from models import Person

app = FastAPI()


class DB:
    def __init__(self, db_url: str):
        self.db_url = db_url

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data


db = DB("ec_people.db")


@app.get("/", response_class=HTMLResponse)
def root():
    with open("demo.html", "r") as f:
        return f.read()


@app.get("/people")
def get_people():
    get_people_query = """
    SELECT * FROM person
    """
    data = db.call_db(get_people_query)
    return data


@app.post("/create_person")
def create_person(person: Person):
    create_person_query = """
    INSERT INTO person ( 
        name, 
        title, 
        email, 
        phone 
    ) VALUES (
        ?, ?, ?, ?
    )
    """
    print(person)
    db.call_db(
        create_person_query,
        person.name,
        person.title,
        person.email,
        person.phone_number,
    )
    return "Created person"
