import sqlite3

# connection = sqlite3.connect("test.db")

# cursor = connection.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test3 (id INTEGER PRIMARY KEY)")
# cursor.execute("CREATE TABLE IF NOT EXISTS test4 (id INTEGER PRIMARY KEY)")
# res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchall())
# cursor.execute("DROP TABLE IF EXISTS test")
# cursor.execute("DROP TABLE IF EXISTS test2")
# cursor.execute("DROP TABLE IF EXISTS test3")
# res2 = cursor.execute("DROP TABLE IF EXISTS test4")
# res = cursor.execute("SELECT name FROM sqlite_master")
# print(res.fetchall(), res2.fetchall())
# cursor.close()
# connection.close()


def call_db(query: str, *args):
    print(args)
    connection = sqlite3.connect(
        "c:/Users/anton/Teaching/DS_22_resources/solutions/testing.db"
    )
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data


# query = """
# CREATE TABLE IF NOT EXISTS test(
#     id INTEGER PRIMARY KEY
# )
# """
# query = """
# DROP TABLE  test
# """
query = """
CREATE TABLE IF NOT EXISTS book(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR (255),
    author VARCHAR (255)
);
"""
data = call_db(query)

# query = """
# INSERT INTO book (title, author) VALUES (?, ?);
# """
# data = call_db(query, "Medmänniskor", "Stefan Einhorn")
# data = call_db(query, "The Audacity of Hope", "Barack Obama")

# query = """
# SELECT * FROM book
# WHERE id = '1';
# """
# data = call_db(query)

# print(data)
