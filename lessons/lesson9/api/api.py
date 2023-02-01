from typing import Dict
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from db import DB
from models import Person

app = FastAPI()
db = DB("book_api.db")


@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()


@app.get("/persons/{id}")
def get_person_by_id(id: int):
    data = db.get(table="person", where=("id", str(id)))
    return data


@app.get("/persons")
def get_persons():
    data = db.get(table="person")
    return data


@app.post("/create_person")
def create_user(person: Person):
    print(person)
    db.insert(table="person", fields={"name": person.name, "age": str(person.age)})
    return "Successfully created"


@app.delete("/delete_person/{id}")
def delete_person(id):
    db.delete(table="person", id=id)


@app.put("/update_person")
def update_person(person: Person):
    data = db.update(
        table="person",
        fields={"name": person.name, "age": str(person.age)},
        where=("id", str(person.id)),
    )
    return data


@app.delete("/delete_person_again")
def delete_person(id: Dict[str, int]):
    db.delete(table="person", id=id["id"])
