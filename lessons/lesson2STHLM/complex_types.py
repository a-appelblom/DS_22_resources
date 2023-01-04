# List

print("______________List / String________________")
list1 = list()
list2 = list([1, "hello", True, None])

list3 = []
list4 = [2, "World", False, 2, 2, 2, 2, "World", False, False]
list5 = [list2, list4]

list6 = list2.copy()

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
list6.append("Fiskmås")
print(hex(id(list2)))
print(hex(id(list6)))


print(list2[1] + " " + list4[1])

length = len(list2)
print(length)

print(list2[len(list2)-1])
print(list2[-1])

string = "Anton"
string_length = len(string)

print(string_length)

print(string[0])

list2[-1] = string
print(list2)

# Funkar inte då strängar är immutable.
# string[2] = "d"
# print(string)

sliced_list2 = list2[1:3]
print(sliced_list2)

sliced_string = string[1:3]
print(sliced_string)

list1.append("Hello, world!")
list1.append("Hello, world Again!")
print(list1)

list1.insert(1, "my")
print(list1)

# Set
print("")
print("______________SET________________")

set1 = {1, 2, 3, 4}
set2 = {}
set3 = set()
set4 = set(list4)

print(set1, type(set1))
print(set2, type(set2))
print(set4, type(set4))

print(set4.pop())
print(set4.pop())
print(set4.pop())

# Tuple
print("")
print("______________Tuple________________")

tuple1 = ()
tuple2 = tuple()

tuple3 = (1, 2, 3, "Hello", "World", False)
tuple4 = tuple((4, 5, 6, "Goodbye", "Hell", True))

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

a, b, c, d, e, f = tuple3

print(d, e)

# Dictionaries
# key, value
print("")
print("______________Dict________________")

dict1 = {}
dict2 = dict()

dict3 = {"name": "Anton", "age": 30}
dict4 = dict({"name": "Björne", "age": 50, (1, 2, 3): "korv", 1: "stroganoff"})

print(dict3)
print(dict4)

print(dict3["name"])
print(dict4.get("name"))

# Funkar inte ger error
# print(dict3["fisk"])

# Ger None om det inte finns
print(dict4.get("fisk"))

print(dict4.get((1, 2, 3)))
print(dict4.get(1))

dict3["nationality"] = "SWEDISH"

pet_dict1 = {"name": "Shirokumakun", "color": "White"}
pet_dict2 = {"name": "Biffen", "color": "Brown"}

company = {"name": "Mujina", "logo": "url", "employees": {"name": "Erik"}}

print(pet_dict1, pet_dict2)

dict3["pets"] = [pet_dict1, pet_dict2]

print(dict3)

dict3["company"] = company

print(dict3)
print(dict3["company"])
print(dict3["pets"])

dict5 = dict4.copy()
print(dict5)
print(dict4)

dict5["name"] = "Sven"
print(dict5)
print(dict4)

print(hex(id(dict5)))
print(hex(id(dict4)))

dict_keys = dict5.keys()
dict_values = dict5.values()

print(dict_keys)
print(dict_values)
