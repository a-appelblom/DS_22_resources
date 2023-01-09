# Indentering
# Funktioner
# Definition
# parametrar
# argument (position, namngivna)

def my_function(name, surname, *rest):
    print("In my function ", rest)
    return "Hej " + name


# my_function("Anton", "Appelblom", 1)
# print(my_function("Anton"))


def a_general_function(x, y, *args, is_employed=False, **kwargs):
    # a, b, c, d, e, f, g = args
    a, b, c, d, e = args
    print(kwargs["name"])
    print(is_employed)
    # print(a, g)
    print(a, e)
    print(args, kwargs)


# a_general_function("A", "B", 1, 2, 3, True, False, name="Anton")


def generate_person(name, surname, *attributes, is_employed, hobbies, **kwargs):
    print(name, surname, " is a person with ", attributes)
    print(name, " is ")
    if is_employed:
        print("Employed")
    else:
        print("Unemployed")

    print("Hobbies are:")
    for hobby in hobbies:
        print(hobby)

    print("Other info")
    for key, value in kwargs.items():
        print(key, value)


# generate_person("Anton", "Appelblom", "Patient",
#                 "Weird", "Bearded", is_employed=True, hobbies=["Games", "climbing", "Music", "Code"], can_run_a_marathon=False, can_fly=False)

# Function with no *


def function_without_catchallargs(pos1=None, pos2=None, kw1=None, kw2=None, **kwargs):
    print(pos1, pos2, kw1, kw2, kwargs)
    pass


# function_without_catchallargs(pos1="A", pos2="B", kw1="HEj", kw2="HEj då")
# function_without_catchallargs("A", "B", kw1="HEj", kw2="HEj då")
# function_without_catchallargs("A", "B", "HEj", "HEj då")

# Function with no **


def function_without_catchallkwargs(pos1, pos2=None, kw1=None, kw2=None):
    print(pos1, pos2, kw1, kw2)
    pass


# function_without_catchallkwargs(pos1="Sven", kw2="kalle")
# function_without_catchallkwargs(kw2="kalle")

def a_function_that_returns_an_int():
    return 1


def a_function_that_returns_an_string():
    return "hej jag heter Anton"


# print(a_function_that_returns_an_int(), type(a_function_that_returns_an_int()))
# print(a_function_that_returns_an_string(),
#       type(a_function_that_returns_an_string()))

def a_function_that_returns_an_list(a, b, c):
    return [a, b, c]


my_list = a_function_that_returns_an_list(1, 2, 3)
# print(my_list)
# print(a_function_that_returns_an_list("Hej", "På", "Dig"))


def a_function_that_returns_an_tuple(a, b, c):
    return (a, b, c)


# my_tuple = a_function_that_returns_an_tuple("A", "B", "C")
value1, value2, value3 = a_function_that_returns_an_tuple("A", "B", "C")
# print(my_tuple)
# print(value1)
# print(value3)


def add_value(value1, value2, *args):
    result = value1 + value2
    for value in args:
        result += value

    return result


my_result = add_value(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
my_result2 = add_value("a", "b", "c", "d")
print(my_result)
print(my_result2)
