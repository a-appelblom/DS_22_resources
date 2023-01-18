from dataclasses import dataclass
from typing import Callable

# Functions in functions


def function_one():
    print("Function one called")
    return "Function one returned"


# function_one()

# En funktion kan sparas i en variabel
function_three_that_is_function_one = function_one

# den Variabeln kan sedan anroppas för att anv'da funktionen
# function_three_that_is_function_one()


def function_two(inner_function: Callable):
    print("Function two called")
    print("Before inner function")
    print(inner_function())
    print("After inner function")


# function_two(inner_function=function_one)

# function_two(inner_function=lambda: "Hello from lamda")

# Lambda functions


# @function_two
# def function_4():
#     print("Function 4 called")


@dataclass
class MyClass:
    a: str
    b: int
    c: float
    pass


# my_onbject = MyClass()

# Closure / scope
# Världen är inte alltid tillgängliga. En funktion har lokala variabler och påverkar inte de utanför.

res = 90


def a():
    res = 0
    for i in range(2):
        res += i

    print(res)
    return res


# print(res)
# res = a()
# print(res)


# def decorator(inner_func: Callable):

#     def wrapper(args, **kwargs):
#         return a
#     return wrapper


# @decorator
# def add(b: int):
#     return


# List, dict comprehension

list = [{"name": "Anton", "age": 30}, {"name": "Pelle", "age": 40},
        {"name": "Stefan", "age": 45}, {"name": "Evert", "age": 90}]

# Ta namnet för varje person och lägg i en ny lista
names = [person["name"] for person in list]

# Ta åldern för varje person och lägg i en ny lista
ages = [person["age"] for person in list]


first_letters = [name[0] for name in names]
all_letters = [letter for name in names for letter in name]

# print(names)
# print(ages)
# print(all_letters)
# print(first_letters)

# Skapar en dict med name som key och age som value
dicts = {names[x]: ages[x] for x in range(len(names))}

# print(dicts)

# While loops, conditions, if statements

# counter = 0
# while True:
#     if counter > 10:
#         break
#     print("I am true with break", counter)
#     counter += 1

# # Vi måste påverka vårat condition i vår loop, vi kan ha fler conditions
# name = "hola"
# counter = 0
# while counter <= 10 and name != "anton":
#     print("I am true with condition", counter)
#     if counter == 5:
#         name = "anton"
#     counter += 1


# Funktioner med args och kwargs
def major_function(*args, **kwargs):
    print("Major function")
    print(args, kwargs)
    pass


def general_function(name, *args, **kwargs):
    print(args, kwargs)
    surname, *rest = args
    fisk = kwargs['fisk']
    print(name, surname, fisk, rest)
    major_function(*rest, **kwargs)
    pass


general_function("Anton", "Appelblom", "Är", "Inte",
                 "Pigg", "På", "Morgonen", fisk="Gös")
