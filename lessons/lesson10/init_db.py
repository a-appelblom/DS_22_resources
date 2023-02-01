import sqlite3
from api import DB

db = DB("ec_people.db")

create_person_table = """
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    name TEXT,
    title TEXT,
    email TEXT,
    phone TEXT
)
"""

db.call_db(create_person_table)
