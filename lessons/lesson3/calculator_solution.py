from typing import Tuple

global OPERATIONS
OPERATIONS = ['+', '-', '*', '/']


def addition(num1: int, num2: int):
    return num1 + num2


def subtraction(num1: int, num2: int):
    return num1 - num2


def multiplication(num1: int, num2: int):
    return num1 * num2


def division(num1: int, num2: int):
    while num2 == 0:
        print("kan inte dividera med 0")
        num1, num2 = get_input(prev_value=num1)
    return num1 / num2


def get_input(prev_value: int | float | None) -> Tuple[int | float, int]:
    valid = False
    if prev_value != None:
        valid = True
        validated1 = prev_value
    while not valid:
        choice1 = input("Vilket är ditt första nummer?: ")
        valid = validate_input(choice1.strip())
        if valid:
            validated1 = int(choice1.strip())
    valid = False
    while not valid:
        choice2 = input("Vilket är ditt andra nummer?: ")
        valid = validate_input(choice2.strip())
        if valid:
            validated2 = int(choice2.strip())

    return (validated1, validated2)


def validate_input(choice_string: str) -> bool:
    valid = str.isdigit(choice_string)
    if not valid:
        print("Felaktigt input")
    return valid


def get_operation() -> str:
    global OPERATIONS
    valid = False
    while not valid:
        operation = input(
            "Vilken beräkning vill du göra? ('+', '-', '*' eller '/'): ")
        operation = operation.strip()
        if operation in OPERATIONS:
            valid = True
    return operation


def get_continue() -> bool:
    while True:
        choice = input("Vill du fortsätta? ('y'/'n'): ")
        if choice == "y":
            return True
        if choice == "n":
            return False


def get_re_use_res() -> bool:
    while True:
        choice = input("Vill du återanvända resultatet? ('y'/'n'): ")
        if choice == "y":
            return True
        if choice == "n":
            return False


def main():
    print("Kalkylator")

    will_continue = True
    res = None
    reuse = False
    while will_continue:
        if not reuse:
            res = None
        num1, num2 = get_input(prev_value=res)
        operation = get_operation()

        if operation == "+":
            res = addition(num1, num2)
        elif operation == '-':
            res = subtraction(num1, num2)
        elif operation == '*':
            res = multiplication(num1, num2)
        elif operation == '/':
            res = division(num1, num2)
        print(res)

        will_continue = get_continue()
        if not will_continue:
            break
        reuse = get_re_use_res()


main()
