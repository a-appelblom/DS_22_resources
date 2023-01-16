from dataclasses import dataclass
from imports.card import Card


class Person:
    age: int
    name: str
    __spy_name: str

    def __init__(self, name: str, age: int, spy_name: str):
        self.name = name
        self.age = age
        self.__spy_name = spy_name

    def get_spy_name(self):
        return self.__spy_name

    def set_spy_name(self, spy_name: str):
        self.__spy_name = spy_name

    def __shoutout_spy_name(self):
        print(self.__spy_name.upper())

    def let_it_out_shoutout(self):
        self.__shoutout_spy_name()

    @staticmethod
    def say_hi(name: str):
        print("Hi", name)


anton = Person("Anton", 30, "Beardboy")

# anton.name = "Evert"
# anton.__spy_name = "Weirdboy"

# print(anton.name)
# print(anton.__spy_name)
# print(anton.get_spy_name())
anton.set_spy_name("HeyBoy")
# print(anton.get_spy_name())

# anton.__shoutout_spy_name()
# anton.let_it_out_shoutout()

# anton.say_hi("My friend")

# Static methods


class Calculator:

    @staticmethod
    def add(a, b):
        return a+b

    @staticmethod
    def subtract(a, b):
        return a-b

    @staticmethod
    def multiply(a, b):
        return a*b

    @staticmethod
    def divide(a, b):
        return a/b


# res = Calculator.add(1, 2)
# print(res)
# res = Calculator.subtract(1, 2)
# print(res)
# res = Calculator.multiply(1, 2)
# print(res)
# res = Calculator.divide(1, 2)
# print(res)

# my_calc = Calculator()

# res = my_calc.add(10, 15)
# print(res)


# Dataclass måste ha attributen definerade och med typen definerad.
@dataclass(init=True, repr=True, kw_only=True)
class Animal:
    name: str
    height: float
    weight: float
    diet: str

    def update_name(self, name):
        self.name = name

    # def __str__(self):
    #     return "Hello"


@dataclass(kw_only=True)
class Dog(Animal):
    race: str
    pass


@dataclass
class Cat(Animal):
    fur: str
    pass


mouse = Animal(name="Mouse", height=5, weight=300, diet="Omnivore")

mouse.update_name("Rat")

print(anton)
print(mouse)

fido = Dog(race="Dalmatian", name="Fido",
           weight=5000, height=100, diet="Omnivore")
print(fido)

meowson = Cat(fur="Naked", diet="Carnivore", height="300",
              weight="1000", name="Moewson")
print(meowson)
