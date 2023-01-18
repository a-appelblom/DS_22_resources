from typing import List


class InvalidChoiceError(Exception):
    pass


class Lesson:
    duration: int
    title: str
    description: str

    def __init__(self, duration: int, title: str, description: str):
        self.duration = duration
        self.title = title
        self.description = description


class Student:
    name: str

    def __init__(self, name: str):
        self.name = name

    # def __str__(self):
    #     string = ""
    #     return string


class Teacher:
    def __init__(self, name: str, company: str, email: str, skills: List[str]):
        self.name = name
        self.company = company
        self.email = email
        self.skills = skills


class Course:
    name: str
    code: str
    credits: int
    teacher: Teacher
    students: List[Student]
    lessons: List[Lesson]

    def __init__(self, name: str, code: str, credits: int, teacher: Teacher, students: List[Student], lessons: List[Lesson]):
        self.name = name
        self.code = code
        self.credits = credits
        self.teacher = teacher
        self.students = students
        self.lessons = lessons

    def __str__(self):
        lessons = ""
        for lesson in self.lessons:
            lessons += lesson.title + ", "
        students = ""
        for student in self.students:
            students += student.name + " "
        string = f"Kurs: {self.name} \n"
        string += f"Kurskod: {self.code} \n"
        string += f"Poäng: {self.credits} \n"
        string += f"Teacher: {self.teacher.name} {self.teacher.email} \n"
        string += f"Students: {students} \n"
        string += f"Lessons: {lessons} \n"
        return string

    def update_teacher(self, teacher: Teacher):
        self.teacher = teacher

    def add_student(self, student: Student):
        self.students.append(student)

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)


def print_choices(choices):

    for i, choice in enumerate(choices):
        print(f"{i}: {choice}")


def run_choice(choice: int, course: Course):
    if choice == 0:
        exit()
    elif choice == 1:
        new_teacher = Teacher(
            "Madeleine", "EC", "somethinh@Something.com", ["Teaching", "Talking", "Guiding"])
        course.update_teacher(new_teacher)
    elif choice == 2:
        new_student = Student("NewGuy")
        course.add_student(new_student)
    elif choice == 3:
        new_lesson = Lesson(1, "New Stuff", "Vi gör nya saker")
        course.add_lesson(new_lesson)
    elif choice == 4:
        print(course)


def main():
    choices = ["Avsluta",
               "Lägg till en lärare till en kurs",
               "Lägg till en elev till en kurs",
               "Lägg till en lektion till en kurs",
               "Skriv ut en kurs"]
    lessons = [Lesson(5, "Repetitionsföreläsning",
                      "Vi går igenom och repeterar allt vi lärt oss hittils på kursen"),
               Lesson(6, "Klasser", "Vi lär oss hur vi använder klasser")]
    students = [Student("Sven"), Student("Erik"),
                Student("Thomas"), Student("Kajsa")]
    teacher = Teacher("Anton", "Mujina", "anton@mujina.se", [
        "Python", "Javascript", "c++", "Agile"])
    course = Course("Python Programmering",
                    "DS_22_python", 40, teacher, students, lessons)

    while True:
        print_choices(choices)
        choice_string = input("Välj ett alternativ: ")
        try:
            choice_string = choice_string.strip()
            choice_int = int(choice_string)
            if not 0 <= choice_int < len(choices):
                raise InvalidChoiceError
        except ValueError:
            print("Not a valid number")
        except InvalidChoiceError:
            print("Not a valid choice")
        else:
            run_choice(choice_int, course)


main()
