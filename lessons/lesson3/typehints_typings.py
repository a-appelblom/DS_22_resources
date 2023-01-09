from typing import Tuple, List, Dict
from enum import Enum
from datetime import datetime, date, time
# from typing import *
# Tuple   # (Vi vet inte var den kommer från)
# import typing
# typing.Tuple

# De vanliga datatyperna finns också
# int, str, float, bool, None


def my_function(a: Tuple[int, str, bool], b: List[int], c: Dict[str, Dict[str, Tuple[int, int]]]):
    print(a, b)


# my_function((1, "hello", True), [1, 2, 3])


def a_new_function(a: int) -> int:
    return a * a


print(a_new_function(1))

EmploymentStatus = Enum('EmploymentStatus', [
                        'unemployed', 'employed', 'let_go'])


# class EmploymentStatus(Enum):
#     let_go = "let_go",
#     unemployed = "unemployed"


person: Dict[str, any] = {
    "name": "Anton",
    "employment_status": EmploymentStatus.let_go,
    "born": date(1992, 2, 5)
}

list_of_employees = [person, person]

print(list_of_employees[0]["born"])
