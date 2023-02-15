from dotenv import load_dotenv

load_dotenv()

import os
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


connection_details = {
    "host": os.getenv("HOST"),
    "user": os.getenv("USR"),
    "passwd": os.getenv("PASSWORD"),
    "db": os.getenv("DATABASE"),
    "ssl": {"ca": os.getenv("MYSQL_ATTR_SSL_CA")},
}

engine = create_engine("mysql+mysqldb://", connect_args={**connection_details})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
