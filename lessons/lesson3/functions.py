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


a_general_function("A", "B", 1, 2, 3, True, False, name="Anton")


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


generate_person("Anton", "Appelblom", "Patient",
                "Weird", "Bearded", is_employed=True, hobbies=["Games", "climbing", "Music", "Code"], can_run_a_marathon=False, can_fly=False)
