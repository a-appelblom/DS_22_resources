# List

print("______________List / String________________")
list1 = list()
list2 = list([1, "hello", True, None])

list3 = []
list4 = [2, "World", False, 2, 2, 2, 2, "World", False, False]

print(list1)
print(list2)
print(list3)
print(list4)

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
