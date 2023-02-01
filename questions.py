# Alla era morgonfrågor på en och samma plats

# Hur fungerar pop funktionen på en lista.

# people = ["Anton", "Erik", "Maja", "Amanda"]
# print(people)

# # Efter pop finns inte elementet kvar i listan
# # Men det returneras och kan sparas i en variabel.
# person = people.pop()

# print(people)
# print(person)

# people.append("Sven")
# print(people)

# from dataclasses import dataclass
# from typing import List


# @dataclass
# class Person:
#     name: str
#     age: int


# class ClassList:
#     students: List[Person] = []

#     def add_person(self, person: Person):
#         self.students.append(person)

#     def __str__(self):
#         string_rep = ""
#         for person in self.students:
#             string_rep += f"Name: {person.name}, age: {person.age} \n"

#         return string_rep

#     def get_students_string(self):
#         string_rep = ""
#         for person in self.students:
#             string_rep += f"Name: {person.name}, age: {person.age} \n"

#         return string_rep


# classList = ClassList()

# classList.add_person(Person("Anton", 30))
# classList.add_person(Person("Pelle", 120))
# classList.add_person(Person("Erik", 20))
# classList.add_person(Person("Anton", 40))
# classList.add_person(Person("Sven", 90))

# print(classList)


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


@app.get("/populate")
def root():
    populate_database()
    return "Populated"


@app.get("/persons")
def get_people():
    person_query = """
    SELECT * FROM person
    """
    persons = call_db(person_query)

    return persons


@app.post("/post_person")
def post_person():
    return "Post person"
