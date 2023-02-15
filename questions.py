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
# import sqlite3
# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# def call_db(query: str, *args):
#     connection = sqlite3.connect("api.db")
#     cursor = connection.cursor()
#     res = cursor.execute(query, args)
#     data = res.fetchall()
#     cursor.close()
#     connection.commit()
#     connection.close()
#     return data


# def populate_database():
#     connection = sqlite3.connect("api.db")
#     cur = connection.cursor()
#     cur.execute(
#         "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,  name varchar(255) NOT NULL)"
#     )
#     cur.execute("INSERT INTO person (name) VALUES ( 'Anton' )")
#     cur.execute("INSERT INTO person (name) VALUES ( 'Erik' )")
#     cur.execute("INSERT INTO person (name) VALUES ( 'Karl' )")
#     cur.close()
#     connection.commit()
#     connection.close()


# @app.get("/populate")
# def root():
#     populate_database()
#     return "Populated"


# @app.get("/persons")
# def get_people():
#     person_query = """
#     SELECT * FROM person
#     """
#     persons = call_db(person_query)

#     return persons


# @app.post("/post_person")
# def post_person():
#     return "Post person"


# @app.get("/persons/{query}")
# def get_person(
#     query: int | str,
# ):  # Detta kallas en union type och är bara ok i python 3.10 och högre eller 3.6 och högre med import från typing
#     pass


# from sqlalchemy import create_engine, text
# from sqlalchemy.engine import URL

# db_server = "LAPTOP-ET0060J7"
# db_name = "test"
# db_driver = "ODBC Driver 17 for SQL Server"

# conn_url = URL.create(
#     "mssql+pyodbc",
#     host=db_server,
#     database=db_name,
#     query={"trusted_connection": "yes", "driver": db_driver},
# )
# engine = create_engine(conn_url)

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE testing (id INT PRIMARY KEY)"))
#     conn.commit()

# from random import shuffle

# # import random

# test: complex = ["a", "b", "c", "d", "e", "f"]

# test2 = complex(real=2, imag=1)


# shuffle(test)
# print(type(test))
# print(test2)
# print(type(test2))

import pandas as pd

my_dict = {"test": [1, 2], "test2": ["Test", "testing"]}

df = pd.DataFrame(my_dict)
print(df)

print(type(df))

my_json = df.to_json()

print(my_json)
