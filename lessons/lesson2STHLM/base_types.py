# Grundläggande datatyperna
print("")
print("______________Datatyper___________________")

a_whole_number: int = 25
a_floating_point_number: float = 2.5
a_string: str = "Anton's, world!"
a_boolean: bool = True  # False
a_whole_lotta_a_nothin: None = None

print(f"Integer: {a_whole_number} - Type: {type(a_whole_number)}")
print(
    f"Float: {a_floating_point_number} - Type: {type(a_floating_point_number)}")
print(f"String: {a_string} - Type: {type(a_string)}")
print(f"Boolean: {a_boolean} - Type: {type(a_boolean)}")
print(
    f"None: {a_whole_lotta_a_nothin} - Type: {type(a_whole_lotta_a_nothin)}")

# Aritmetik
# INT
# En int vid operationer addition. subtration, multiplikation
# En operation där andra talet är en float blir en float och även division mellan 2 integers blir en float
print("")
print("______________INT___________________")

int1 = 10
int2 = 5
test_float = 2.5

int3 = int1 + int2
print(int3, type(int3))

int3 = int2 - int1
print(int3, type(int3))

int3 = int1 * int2
print(int3, type(int3))

int3 = int1 / int2
print(int3, type(int3))

int3 = int1 + test_float
print(int3, type(int3))

# Float
# All aritmetik med floats resulterar i en float
print("")
print("______________Float___________________")

float1 = 2.0
float2 = 1.5

float3 = float1 + float2
print(float3, type(float3))

float3 = float2 - float1
print(float3, type(float3))

float3 = float1 * float2
print(float3, type(float3))

float3 = float1 / float2
print(float3, type(float3))

float3 = int1 + float1
print(float3, type(float3))

# String
print("")
print("______________String___________________")

string1 = "Anton"
string2 = 'Hej'

string3 = string1 + string2
print(string3, type(string3))

# Funkar inte
# string3 = string2 - string1
# print(string3, type(string3))

# Funkar inte
# string3 = string1 * string2
# print(string3, type(string3))

string3 = string1 * int1
print(string3, type(string3))

# Funkar inte
# string3 = string1 / string2
# print(string3, type(string3))

# Funkar inte
# string3 = int1 + string1
# print(string3, type(string3))

# Funkar inte
# string3 = float1 + string1
# print(string3, type(string3))

# Booleans
print("")
print("______________Booleans___________________")

bool1 = True
bool2 = False

bool3 = bool1 + bool2
print(bool3, type(bool3))

bool3 = bool2 - bool1
print(bool3, type(bool3))

bool3 = bool1 * bool2
print(bool3, type(bool3))

# Funkar inte eftersom det är division med 0
# bool3 = bool1 / bool2
# print(bool3, type(bool3))

bool3 = bool2 / bool1
print(bool3, type(bool3))

bool3 = int1 + bool1
print(bool3, type(bool3))

bool3 = float1 + bool1
print(bool3, type(bool3))


# None
# Inga operationer
print("")
print("______________None___________________")

none1 = None

# Funkar inte
# test = int1 + none1
# print(test)

# Casting

print("")
print("______________Casting___________________")


floater = 1.0
inter = 1
inter2 = 0
stringer = "1"
stringer2 = "1.5"
booler = True
booler2 = False

print(int(floater))
print(float(inter))
print(int(stringer))
# print(int(stringer2))
print(float(stringer))
print(float(stringer2))

print(bool(inter))
print(bool(inter2))

print(int(booler))
print(int(booler2))

print(float(booler))
print(float(booler2))

print(str(floater))
print(str(inter))
print(str(booler))
