# Operatorer

# Andra språk ||, &&
# Python or, and
anton = {"name": "antonia", "age": 15, "description": "developer"}
name = "Antonio"

truth = name == "Anton"

print(truth)

truth = anton["age"] > 30
print(truth)

truth = anton["age"] >= 30
print(truth)

truth = anton["age"] < 30
print(truth)

truth = anton["age"] <= 30
print(truth)

truth = anton["age"] <= 30 and anton["name"] == "Antonio"
print(truth)

truth = anton["age"] <= 30 or anton["name"] == "Antonio"
print(truth)

truth = anton["age"] <= 30 or not anton["name"] == "Antonio"
print(truth)

truth = anton["age"] <= 30 and not anton["name"] == "Antonio"
print(truth)

truth = anton["age"] <= 30 and not anton["name"] != "Antonio"
print(truth)

# If

if False:
    print("Its the truth and nothin but the truth")

if anton["name"] == "antonio":
    print("What an impostor")

elif anton["name"] == "anton":
    print("Its the truth and nothin but the truth")

elif anton["age"] > 20:
    print("T'is him")

else:
    print("Something else")

a_zero = 0
a_one = 1
a_none = None
an_empty_string = ""
a_string = " "

if not a_zero:  # Noll blir ett false värde
    print("Zero is true")

if a_one:  # Postitiva och negativa siffror får true
    print("one is true")

if not a_none:  # None evalueras til false då det är ingenting
    print("None is true")

if not an_empty_string:  # Tom sträng bli false
    print("String is true")

if a_string:  # Bara ett tecken i en sträng gör att den blir true även om det är ett blanksteg.
    print("String is true")
