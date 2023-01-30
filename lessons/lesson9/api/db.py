import sqlite3
import os
from typing import Dict


class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url
        if not os.path.exists(self.db_url):
            self.__set_up_db()

    def __set_up_db(self):
        conn = sqlite3.connect(self.db_url)
        with open("setup.sql", "r") as file:
            script = file.read()
            conn.executescript(script)
            conn.commit()

        conn.close()

    def __call_db(self, query):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data

    def insert(self, *, table: str, fields: Dict[str, str]):
        # Skapa en query
        # MEd värden från vårat anrop
        # Anropa databasen

        keys = ",".join(fields.keys())
        values = "','".join(fields.values())

        query = f"""
        INSERT INTO {table} (
            {keys}
        ) VALUES (
            '{values}'
        )
        """
        return self.__call_db(query)
