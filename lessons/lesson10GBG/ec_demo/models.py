from pydantic import BaseModel


class Person(BaseModel):
    name: str
    title: str
    mail: str
    tel: str
