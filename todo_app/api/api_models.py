from datetime import datetime
from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str
    due_date: datetime
    completed: bool


class Login(BaseModel):
    email: str
    password: str


class User(BaseModel):
    id: int = None
    email: str
    display_name: str
    todos: List[Todo]
