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

with open("seed.json", "r") as seed:
    data = json.load(seed)

    for todo in data:
        db.call_db(create_todo, todo["title"], todo["description"])
