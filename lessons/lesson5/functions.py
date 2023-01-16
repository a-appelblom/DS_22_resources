def a_function():
    print("A function")


def another_function():
    print("Another function")


a_variable = a_function
# another_function = a_function


# a_function()
# another_function()
# a_variable()

# print(a_function, a_variable)

def first_function(a):
    print(a(1, 2))
    print("First function", a)


def second_function(a, b):
    print("Second function")
    return "Hola"


# first_function("Hej")
first_function(second_function)


# En lambda-function är en anonym funktion
def my_lambda(a, b):
    return a + b


# print(my_lambda(1, 2))

first_function(lambda a, b: a+b)

people = [{"name": "Anton", "age": 30},
          {"name": "Kalle", "age": 45},
          {"name": "Gurra", "age": 12}]

print(sorted(people, key=lambda a: a['age']))


def compare_name(b):
    return b["name"]


print(sorted(people, key=compare_name))
