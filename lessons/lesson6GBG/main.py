# Klasser
# Vanlig klass, init, magic_methods, methods, arguments, instans/klass/objekt vad är vad, arv vs komposition.

from dataclasses import dataclass

# objekt
# samlingar data och metoder

# Klass
# Är en ritning för ett objekt

# Instans
# En instans är ett objekt av en specifik klass

# Arv vs komposition
# En lärare 'r en person, men alla personer är inte lärare. Typexempel för när arv är rimligt.
# En kortlek är inte en färlänging av kort, utan är en samling av kort. Här är det komposition, där en lek alltså har flera kort.


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

    def calculate_age_from_birthyear(self, year: int, *args, **kwargs) -> int:
        print(args, kwargs)
        return 2023 - year


class Teacher(Person):
    pass


class Student(Person):
    pass


my_dude = Person("Anton", 30)
# my_dude = Person()
my_dude.add_name("John")
# print(my_dude.calculate_age_from_birthyear(1992, "a", "r", "g", "s", k="k"))

# print(my_dude.__dict__)
# print(my_dude.get_years_per_letter())

# Dataclasses
# Dataclasses är skönt för att snabbt skapa upp logiska samlingar med data.
# Behövs extra logik vid initeringen kan en dataclass vara onödigt.


@dataclass
class DataPerson:
    name: str
    age: int

    # def __init__():
    #     pass


my_data_dude = DataPerson("Fjanton", 156)

# print(my_data_dude)


@dataclass
class Animal(object):
    tooth_count: int
    color: int
    size: str


@dataclass
class Dog(Animal):
    # def __init__(self):
    #     pass

    def bark(self):
        print("Woof")


@dataclass
class Fish(Animal):
    habitat: str
    fin_count: int

    # def __init__(self, habitat, fin_count):
    #     pass


# guppy = Fish()


fido = Dog(4, "Gray", "Medium")

# print(fido)

# Funktioner, args, kwargs


def my_function(self, *args, other, **kwargs):
    print(self, other)
    print(f"my_function({args}, {kwargs})")


def my_second_function(func, *args, **kwargs):
    a, b, *rest = args
    print(a, b)
    print(rest)
    func(*rest, **kwargs)

# Print är ett exempel på när obestämt antal argument kan skickas in.
# print("a", "a", "a", "a", "a")


# my_function("Anton", "Är", "Trött", other="else", reason="Late nights")

# my_second_function(my_function, "Anton", "Är", "Trött", "På", "Morgonen",
#                    other="else", reason="Late nights")


# Error
# Error är egenligen bara klasser och objekt.

# print(Exception)
# print(ValueError.__base__)


class MyError(Exception):
    pass


# print(MyError.__base__)

# num = 1000
# try:
#     if num == 0:
#         raise ValueError
#     elif num == 1:
#         raise MyError
#     elif num == 2:
#         raise Exception
#     else:
#         raise

# except ValueError:
#     print("value error")
# except MyError:
#     print("My error")
# except Exception:
#     print("Regular ol' exception")
# except:
#     print("All exceptions")
# else:
#     print("All is well")


# List and dict comprehension

people = [{"name": "Anton", "age": 30},
          {"name": "Karl", "age": 5},
          {"name": "Erik", "age": 31},
          {"name": "Francis", "age": 67}]

print(people)

names = [person['name'] for person in people]
ages = [person['age'] for person in people]
all_letters = [letter for name in names for letter in name]
# letters = [letter for person in people for letter in person]
# letters = [letter for person['name'] in names for person in people]

print(names, ages)
print(all_letters)

my_people = {person["name"]: person["age"] for person in people}
my_other_people = {names[x]: ages[x] for x in range(len(names))}

print(my_people)
print(my_other_people)
