import sqlite3


class DB:
    db_url: str

    def __init__(self, db_url: str):
        self.db_url = db_url

    def call_db(self, query, *args):
        conn = sqlite3.connect(self.db_url)
        cur = conn.cursor()
        res = cur.execute(query, args)
        data = res.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return data
