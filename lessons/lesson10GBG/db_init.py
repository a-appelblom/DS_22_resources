from db import DB

db = DB("people.db")

create_people_table_query = """
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT,
    title TEXT,
    tel TEXT,
    mail TEXT
    )
"""
db.call_db(create_people_table_query)
