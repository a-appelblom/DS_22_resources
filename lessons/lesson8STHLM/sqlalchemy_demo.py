from sqlalchemy import (
    create_engine,
    Table,
    Column,
    String,
    Integer,
    MetaData,
    ForeignKey,
    insert,
)
from sqlalchemy.orm import declarative_base


engine = create_engine("sqlite:///test.db")
meta_data = MetaData()

user_table = Table(
    "user",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
)

director = Table(
    "director",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("age", Integer),
    Column("company", String),
)

movie_table = Table(
    "movie",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("year", Integer),
    Column("director", ForeignKey("director.id")),
)


meta_data.create_all(engine)


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)


# print(engine)

# connection = engine.connect()

# res = connection.execute("SELECT * FROM book")
# print(res.fetchall())
# connection.close()


# with engine.connect() as conn:
#     res = conn.execute("UPDATE book SET title =  'The woods' WHERE id = 18")

# with engine.connect() as conn:
#     res = conn.execute("SELECT * FROM book")
#     print(res.fetchall())


statement = insert(user_table).values(first_name="Anton", last_name="Appelblom")

with engine.connect() as conn:
    conn.execute(statement)

with engine.connect() as conn:
    conn.execute(
        insert(user_table),
        [
            {"first_name": "Erik", "last_name": "Eriksson"},
            {"first_name": "Karl", "last_name": "Karlsson"},
        ],
    )
