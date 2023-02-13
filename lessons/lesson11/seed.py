import json
from db import DB

db = DB("todo.db")

create_todo = """
INSERT INTO todo (
title, 
description
) VALUES (
?, ?
)
"""
create_user = """
INSERT INTO user (
name, 
age
) VALUES (
?, ?
)
"""

with open("seed.json", "r") as seed:
    data = json.load(seed)

    for todo in data["todos"]:
        db.call_db(create_todo, todo["title"], todo["description"])

    for user in data["users"]:
        db.call_db(create_user, user["name"], user["age"])
