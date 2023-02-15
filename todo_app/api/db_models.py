from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from db import Base, engine


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(String(255), index=True)
    due_date = Column(DateTime, index=True)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer)

    # owner = relationship("User", back_populates="todos")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    display_name = Column(String(50), unique=True, index=True)
    password = Column(String(255))

    # todos = relationship("Todo", back_populates="owner", primaryjoin="Todo.id")


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
