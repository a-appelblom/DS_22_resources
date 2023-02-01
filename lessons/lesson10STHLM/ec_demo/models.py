from pydantic import BaseModel


class Person(BaseModel):
    name: str
    title: str
    phone_number: str
    email: str
