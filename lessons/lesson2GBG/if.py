# Logik
anton = {
    "name": "Anton",
    "age": 30,
    "employed": True,
    "company": {
        "name": "Mujina",
        "location": "STHLM",
        "board": {
            "CEO": "Pelle",
            "CTO": "Francois"
        }
    },
    "pets": [
        {
            "name": "Shirokumakun",
            "color": "white",
            "age": 25
        }
    ]
}

# ==, !=, >, >=, <, <=
# and, or, not

truth = 1 + 1 == 2
print(truth, type(truth))

truth = 1 + 1 != 2
print(truth, type(truth))

truth = anton["name"] == "Anton"
print(truth, type(truth))

truth = anton["age"] < 30
print(truth, type(truth))

truth = anton["age"] <= 30
print(truth, type(truth))

truth = anton["age"] > 30
print(truth, type(truth))

truth = anton["age"] >= 30
print(truth, type(truth))

truth = anton["age"] >= 30 and anton["name"] == "Anton"
print(truth, type(truth))

truth = anton["age"] > 30 and anton["name"] == "Anton"
print(truth, type(truth))

truth = anton["age"] > 30 or anton["name"] == "Anton"
print(truth, type(truth))

truth = anton["age"] == 30 and not anton["name"] == "Anton"
print(truth, type(truth))

# If-satser

# Kommer alltid att köras
if True:
    print("It's true")

# Kommer aldrig att köras
if False:
    print("It's true")

if anton["age"] <= 30:
    print("Anton is older than 30")

if not anton["age"] <= 30:
    print("Anton is not older than 30")

if False:
    print("It's false")
elif True:
    print("It is instead true")

if anton["age"] < 30:
    print("What a youngling")
elif anton["age"] > 30:
    print("Age is but a number")
elif anton["age"] != 30:
    print("Living on the edge")
else:
    print("Age is weird")

if anton["age"] == 30 and not anton["name"] != "Anton":
    print("Its anton")

# Värden i datyper kan evalueras i if-satser.

a_zero = 0  # Utvärderas till false
a_none = None  # Utvärderas till false
an_empty_string = ""  # Utvärderas till false

a_one = 1
a_string = " "

if a_zero:
    print("It's a zero")
if a_one:
    print("It's a one")
if a_none:
    print("It's a none")
if an_empty_string:
    print("It's a an empty string")
if a_string:
    print("It's a string")

if not a_zero:
    print("I wanna do stuff")
