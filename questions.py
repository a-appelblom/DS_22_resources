# Alla era morgonfrågor på en och samma plats

# Hur fungerar pop funktionen på en lista.

# people = ["Anton", "Erik", "Maja", "Amanda"]
# print(people)

# # Efter pop finns inte elementet kvar i listan
# # Men det returneras och kan sparas i en variabel.
# person = people.pop()

# print(people)
# print(person)

# people.append("Sven")
# print(people)

from dataclasses import dataclass
from typing import List


@dataclass
class Person:
    name: str
    age: int


class ClassList:
    students: List[Person] = []

    def add_person(self, person: Person):
        self.students.append(person)

    def __str__(self):
        string_rep = ""
        for person in self.students:
            string_rep += f"Name: {person.name}, age: {person.age} \n"

        return string_rep

    def get_students_string(self):
        string_rep = ""
        for person in self.students:
            string_rep += f"Name: {person.name}, age: {person.age} \n"

        return string_rep


classList = ClassList()

classList.add_person(Person("Anton", 30))
classList.add_person(Person("Pelle", 120))
classList.add_person(Person("Erik", 20))
classList.add_person(Person("Anton", 40))
classList.add_person(Person("Sven", 90))

print(classList)
