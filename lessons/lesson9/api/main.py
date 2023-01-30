# FastAPI
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


def call_db(query: str, *args):
    connection = sqlite3.connect("api.db")
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data


def populate_database():
    connection = sqlite3.connect("api.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,  name varchar(255) NOT NULL)"
    )
    cur.execute("INSERT INTO person (name) VALUES ( 'Anton' )")
    cur.execute("INSERT INTO person (name) VALUES ( 'Erik' )")
    cur.execute("INSERT INTO person (name) VALUES ( 'Karl' )")
    cur.close()
    connection.commit()
    connection.close()
    pass


@app.get("/")
def root():
    return "Hello World"


@app.get("/populate")
def root():
    populate_database()
    return "Populated"


@app.get("/test")
def test():
    i = 0
    while True:
        print("Hello World")
        i += 1
        if i > 10:
            break
    return "Hello Test"


@app.get("/test/fisk/banan")
def test2():
    print("THis is my test place")
    return "Hello Test, fisk, banan"


@app.get("/persons")
def get_people():
    person_query = """
    SELECT * FROM person
    """
    persons = call_db(person_query)

    return persons


# @app.get("/person/id/{id}")
# def get_person_by_id(id: int):
#     get_person_query = """
#     select * from person
#     WHERE id = ?
#     """
#     data = call_db(get_person_query, id)
#     return data


# @app.get("/person/name/{name}")
# def get_person_by_name(name: str):
#     get_person_query = """
#     select * from person
#     WHERE name = ?
#     """
#     data = call_db(get_person_query, name)
#     return data


@app.get("/person/")
def get_person(name: str = None, id: int = None):
    # insert_person_query = """
    # insert into person (name) values (?)
    # """
    # call_db(insert_person_query, name) # Dålig praxis
    print(name, id)

    return "Get Person"


class Person(BaseModel):
    name: str
    id: int


@app.post("/persona")
def post_person(person: Person):
    insert_person_query = """
    insert into person (name) values (?)
    """
    call_db(insert_person_query, person.name)  # Dålig praxis
    return person


@app.put("/update_person")
def update_person(person: Person):
    update_person_query = """
    UPDATE person SET name = ? WHERE id = ?
    """
    call_db(update_person_query, person.name, person.id)
    pass


@app.delete("/delete_person/{id}")
def delete_person(id: int):
    delete_person_query = """
    DELETE FROM person WHERE id = ?
    """
    data = call_db(delete_person_query, id)
    return data
