from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    ForeignKey,
    insert,
    select,
)

engine = create_engine("sqlite:///test.db")
meta_data = MetaData()

alchemist_table = Table(
    "alchemist",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("person_id", ForeignKey("person.id")),
)
person_table = Table(
    "person",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("motto", String),
)

meta_data.create_all(engine)

# statement = select(person_table).values(
#     first_name="Anton", last_name="Appelblom", motto="Live damn you tele2"
# )
statement = select(person_table).where(person_table.c.first_name == "Anton")

with engine.connect() as conn:
    res = conn.execute(statement)
    data = res.fetchall()
    print(data)

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

# with engine.connect() as conn:
#     conn.execute(
#         "CREATE TABLE IF NOT EXISTS person (id INTEGER PRIMARY KEY,  first_name VARCHAR(80), last_name VARCHAR(80), motto VARCHAR(255))"
#     )
# with engine.connect() as conn:
#     conn.execute(
#         "INSERT INTO person ( first_name, last_name, motto) VALUES ('Pikachu', 'Pikasson', 'Pika pika')"
#     )

# with engine.connect() as conn:
#     first_name = "Al"
#     last_name = "Appelblom"
#     res = conn.execute(
#         "SELECT * FROM person WHERE first_name = ? OR last_name = ?",
#         (first_name, last_name),
#     )
#     data = res.fetchall()
#     print(data)


# def call_db_sqla(query: str, *args):
#     with engine.connect() as conn:
#         res = conn.execute(query, args)
#         if res:
#             data = res.fetchall()
#             return data


# data = call_db_sqla("SELECT * FROM person WHERE first_name = ?", "Pikachu")
# print(data)

# data = call_db_sqla(
#     "INSERT INTO person (first_name, last_name, motto) VALUES ( ?, ?, ?)",
#     "Sven Bertil",
#     "Taube",
#     "Vet Faktiskt inte",
# )
# print(data)
