from typing import List


class Lesson:
    title: str
    description: str
    time_in_hours: int

    def __init__(self, title: str, description: str, time_in_hours: int):
        self.title = title
        self.description = description
        self.time_in_hours = time_in_hours


class Student:
    name: str

    def __init__(self, name: str):
        self.name = name


class Teacher:
    name: str
    company: str
    skills: List[str]

    def __init__(self, name: str, company: str, skills: List[str]):
        self.name = name
        self.company = company
        self.skills = skills


class Course:
    name: str
    code: str
    credits: int
    teacher: Teacher
    students: List[Student]
    lessons: List[Lesson]

    def __init__(self,
                 name: str,
                 code: str,
                 credits: int,
                 teacher: Teacher,
                 students: List[Student],
                 lessons: List[Lesson]):
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher
        self.students = students
        self.lessons = lessons

    def __str__(self):
        lessons = ""
        for lesson in self.lessons:
            lessons += f"{lesson.title}, "
        students = ""
        # students_list = []
        for student in self.students:
            # students_list.append(student.name)
            students += f"{student.name}, "

        string = f"Kurs: {self.name} \n"
        string += f"Kod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Teacher: {self.teacher.name} \n"
        string += f"Students: {students} \n"
        string += f"Lessons: {lessons} \n"

        return string

    def update_teacher(self, teacher: Teacher):
        self.teacher = teacher

    def add_student(self, student: Student):
        self.students.append(student)

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)


def print_choices(choices: List[str]):

    for i, choice in enumerate(choices):
        print(f"{i}: {choice}")


def run_choice(choice: int, course: Course):
    if choice == 0:
        exit()
    elif choice == 1:
        course.update_teacher(Teacher("Molly", "EC", ["Teaching"]))
    elif choice == 2:
        course.add_student(Student("´NewGuy"))
    elif choice == 3:
        course.add_lesson(Lesson("Learn", "Just do it", 12))
    elif choice == 4:
        print(course)


class NonValidChoiceError(Exception):
    pass


def main():
    course = Course("Python programering",
                    "DS_22_Python", 40,
                    Teacher("Anton",
                            "Mujina",
                            ["Python", "Javascript", "Att inte skriva return"]),
                    [Student("Sven"), Student("Bertil"), Student("Anton")],
                    [Lesson("Repetition", "Vi repeterar allt vi gjort", 4), Lesson("Klasser", "Vi lär oss OOP", 457)])

    choices = ["Exit", "Update teacher",
               "Add student", "Add lesson", "Print course"]
    while True:
        print_choices(choices)
        choice_string = input("Choose an option: ")
        try:
            choice_int = int(choice_string.strip())
            if not 0 <= choice_int < len(choices):
                raise NonValidChoiceError
        except ValueError:
            print("Not a valid number")
        except NonValidChoiceError:
            print("Invalid choice")
        else:
            run_choice(choice_int, course)


main()
