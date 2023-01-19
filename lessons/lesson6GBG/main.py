# Klasser
# Vanlig klass, init, magic_methods, methods, arguments, instans/klass/objekt vad är vad, arv vs komposition.

from dataclasses import dataclass


class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"

    def add_name(self, name: str) -> None:
        self.name = name

    def get_years_per_letter(self) -> float:
        return self.age / len(self.name)


my_dude = Person("Anton", 30)
# my_dude = Person()
my_dude.add_name("John")

# print(my_dude.__dict__)
# print(my_dude.get_years_per_letter())

# Dataclasses


@dataclass
class DataPerson:
    name: str
    age: int

    # def __init__():
    #     pass


my_data_dude = DataPerson("Fjanton", 156)

# print(my_data_dude)

# Funktioner, args, kwargs


def my_function(self, *args, other, **kwargs):
    print(self)
    print(f"my_function({args}, {kwargs})")
    pass


my_function(Anton", "Är", "Trött", reason="Late nights")
