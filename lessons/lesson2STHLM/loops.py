my_list = ["Anton", "Appelblom", "Apples", "Oranges"]

my_dict = {"name": "Anton", "age": 30, "description": "Developer"}

print(my_list)

# For
for string in my_list:
    print(string)

for i in range(5):
    print(i)

for i in range(len(my_list)):
    print(my_list[i])

for i, string in enumerate(my_list):
    print(i, string)

for key in my_dict.keys():
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)

# While
# Det som händer i en while loop, måste påverka det som evalueras.
number = 1
while True:
    number = number + 1
    if number == 5:
        continue
    print(number)
    if number > 10:
        break
