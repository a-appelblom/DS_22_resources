# Loopar
# for, while

number = 0
while True:
    number = number + 1
    print(number)
    if number == 10:
        break

print("after loop1")

number = 0
while number <= 10:
    print(number)
    number = number + 1

print("after loop2")

# Att tänka på med while loopar
# Det condition som styr loopen måste ändras i loopen på något sätt

for palsternacka in range(5, 10, 2):
    print(palsternacka)

my_list = ["En", "Banan", "Var", "Ute", "Och", "Gick"]
my_list2 = ["Två", "Bananer", "Var", "inne", "Och", "Sov"]

for string in my_list:
    print(string)

for i in range(len(my_list)):
    print(my_list[i])
    print(my_list2[i])

for i, string in enumerate(my_list):
    print(i, string)
    print(i, my_list2[i])

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
for key in anton.keys():
    print(key)

for value in anton.values():
    print(value)

for key, value in anton.items():
    print(key, value)
    if type(value) == type(dict()):
        for key, value in anton[key].items():
            print(key, value)
