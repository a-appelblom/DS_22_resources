from fastapi import FastAPI
from pydantic import BaseModel

from db import DB
from models import Person

app = FastAPI()
db = DB("book_api.db")


@app.post("/create_person")
def create_user(person: Person):
    print(person)
    db.insert(table="person", fields={"name": person.name, "age": str(person.age)})
    pass
