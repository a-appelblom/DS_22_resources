import sqlite3

# connection = sqlite3.connect("test.db")
# cursor = connection.cursor()

# cursor.execute(
#     "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name VARCHAR(80))"
# )
# # cursor.execute(
# #     "CREATE TABLE IF NOT EXISTS test2 (id INTEGER PRIMARY KEY, name VARCHAR(80))"
# # )
# # cursor.execute(
# #     "CREATE TABLE IF NOT EXISTS test3 (id INTEGER PRIMARY KEY, name VARCHAR(80))"
# # )

# cursor.execute("INSERT INTO test (name) VALUES ('test2')")
# cursor.execute("INSERT INTO test (name) VALUES ('Anton')")
# cursor.execute("INSERT INTO test (name) VALUES ('Pelle')")
# cursor.execute("INSERT INTO test (name) VALUES ('Lisa')")
# person_query = """
# INSERT INTO test(
#     name
# ) VALUES (
#     'Tove'
# )
# """
# cursor.execute(person_query)

# # res = cursor.execute("SELECT name FROM sqlite_master")
# res = cursor.execute("SELECT name FROM test")
# # data = res.fetchall()
# data = res.fetchone()
# print(data)
# data = res.fetchone()
# print(data)
# data = res.fetchone()
# print(data)
# data = res.fetchone()
# print(data)

# # cursor.execute("DROP TABLE test2")
# # cursor.execute("DROP TABLE test3")

# cursor.close()
# connection.commit()
# connection.close()

# print(data)


def call_db(query: str, *args):
    connection = sqlite3.connect("test.db")
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data


# query = """
# INSERT INTO person(
#     first_name,
#     last_name,
#     motto
# ) VALUES (
#     ?, ?, ?
# )
# """

# data = call_db(query, "Jack", "Sparrow", "Drink")
# print(data)


# query = """
# CREATE TABLE IF NOT EXISTS person (
#     id INTEGER PRIMARY KEY,
#     first_name VARCHAR(80),
#     last_name VARCHAR(80),
#     motto VARCHAR(255)
#     )
# """

# data = call_db(query)
# print(data)

# query = """
# INSERT INTO person (
#     first_name,
#     last_name,
#     motto
# ) VALUES (
#     "Anton",
#     "Appelblom",
#     "42"
# )
# """
# data = call_db(query)
# print(data)

# query = """
# SELECT * FROM person
# WHERE first_name = 'Anton'
# """
# data = call_db(query)
# print(data)
