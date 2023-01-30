from pydantic import BaseModel


class Person(BaseModel):
    id: int
    name: str
    age: int
    favorite_book_id: int = None
