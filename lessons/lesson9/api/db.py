import sqlite3
import os
from typing import Dict, Tuple


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

    def get(self, *, table: str, where: Tuple[str, str] | None = None):
        query = f"""
        SELECT * FROM {table} 
        """
        if where:
            key, val = where
            where_query = f"""
            WHERE {key} = {val}
            """
            query = query + where_query
        data = self.__call_db(query)
        return data

    def delete(self, *, table: str, id: int):
        delete_query = f"""
        DELETE FROM {table} WHERE id = {id}
        """
        self.__call_db(delete_query)

    def update(self, *, table: str, where: Tuple[str, str], fields: Dict[str, str]):
        where_key, where_val = where
        field_query = ""
        for key, val in fields.items():
            field_query += f"{key} = '{val}',"
        field_query = field_query[:-1]
        update_query = f"""
        UPDATE {table} SET {field_query} WHERE {where_key} = '{where_val}' 
        """
        print(update_query)
        return self.__call_db(update_query)
        pass
