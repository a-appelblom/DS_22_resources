from sqlalchemy import create_engine

engine = create_engine("sqlite:///test.db")

# connection = engine.connect()

# res = connection.execute(
#     "CREATE TABLE IF NOT EXISTS alchemist (id INTEGER PRIMARY KEY, name VARCHAR(255))"
# )
# res = connection.execute(
#     "INSERT INTO person (first_name, last_name, motto) VALUES ('Al', 'Capone', 'Mamaaaa')"
# )
# # data = res.fetchall()
# # print(data)

# res = connection.execute("SELECT first_name FROM person")
# data = res.fetchall()
# print(data)

# connection.close()

with engine.connect() as conn:
    conn.execute(
        "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY,  first_name VARCHAR(80), last_name VARCHAR(80), motto VARCHAR(255))"
    )
with engine.connect() as conn:
    conn.execute(
        "INSERT INTO person ( first_name, last_name, motto) VALUES ('Pikachu', 'Pikasson', 'Pika pika')"
    )

with engine.connect() as conn:
    first_name = "Al"
    last_name = "Appelblom"
    res = conn.execute(
        "SELECT * FROM person WHERE first_name = ? OR last_name = ?",
        (first_name, last_name),
    )
    data = res.fetchall()
    print(data)


def call_db_sqla(query: str, *args):
    with engine.connect() as conn:
        res = conn.execute(query, args)
        if res:
            data = res.fetchall()
            return data


data = call_db_sqla("SELECT * FROM person WHERE first_name = ?", "Pikachu")
print(data)

data = call_db_sqla(
    "INSERT INTO person (first_name, last_name, motto) VALUES ( ?, ?, ?)",
    "Sven Bertil",
    "Taube",
    "Vet Faktiskt inte",
)
print(data)
