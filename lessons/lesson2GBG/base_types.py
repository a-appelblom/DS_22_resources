# Grundläggande datatyper
print("")
print("____________DATATYPER____________")

a_whole_number: int = 10
a_floating_point_number: float = 1.5
a_string: str = "Hej jag heter Anton"
a_boolean: bool = True
a_whole_lotta_mothin: None = None

print(f"Integer: {a_whole_number} - Type: {type(a_whole_number)}")
print(
    f"Float: {a_floating_point_number} - Type: {type(a_floating_point_number)}")
print(f"String: {a_string} - Type: {type(a_string)}")
print(f"Boolean: {a_boolean} - Type: {type(a_boolean)}")
print(f"None: {a_whole_lotta_mothin} - Type: {type(a_whole_lotta_mothin)}")

# Aritmetik
print("")
print("____________Int____________")
# Int
# En int kommer att resultera i en int vid addition, subtraction, multiplication
# Division komemr alltid att leda till en float
# Operationer med en float kommer alltid att leda till en float.

int1 = 10
int2 = 5
test_float = 1.5

int3 = int1 + int2
print(int3, type(int3))

int3 = int1 - int2
print(int3, type(int3))

int3 = int1 * int2
print(int3, type(int3))

int3 = int1 / int2
print(int3, type(int3))

int3 = int1 + test_float
print(int3, type(int3))


print("")
print("____________Float____________")
# Float
# Alla beräkningar med en float, blir en float. Annat än om med en sträng då blir det error.

float1 = 1.5
float2 = 6.0

float3 = float1 + float2
print(float3, type(float3))

float3 = float1 - float2
print(float3, type(float3))

float3 = float1 * int2
print(float3, type(float3))

float3 = float1 / float2
print(float3, type(float3))

float3 = int1 + float2
print(float3, type(float3))


print("")
print("____________String____________")
# String


string1 = "Anton"
string2 = "Appelblom"

string3 = string1 + string2
print(string3, type(string3))

# string3 = string1 - string2 # Funkar inte
# print(string3, type(string3))

# string3 = string1 * string2 # Funkar inte
# print(string3, type(string3))

# string3 = string1 / string2 # Funkar inte
# print(string3, type(string3))

# string3 = int1 + string2 # Funkar inte
# print(float3, type(float3))

string3 = int1 * string2
print(string3, type(string3))

print("")
print("____________Booleans____________")
# Booleans
# Booleans blir vid aritmetik andra numberiska datatyper oftast int då de representeras av 1 respektive 0.

boolean1 = True
boolean2 = False

boolean3 = boolean1 + boolean2
print(boolean3, type(boolean3))

boolean3 = boolean1 - boolean2
print(boolean3, type(boolean3))

boolean3 = boolean1 * boolean2
print(boolean3, type(boolean3))

boolean3 = boolean2 / boolean1
print(boolean3, type(boolean3))

boolean3 = int1 + boolean2
print(boolean3, type(boolean3))

boolean3 = int1 * boolean2
print(boolean3, type(boolean3))

print("")
print("____________None____________")
# None
# Går inte att göra några operationer med none.
none1 = None

# result = int1 + none1
# print(result, type(result))

print("")
print("____________Casting____________")

floater = 1.0
inter = 2
inter2 = 0
stringer = "1"
stringer2 = "1.5"
booler = True
booler2 = False

result = int(floater)
print(result, type(result))

result = float(inter)
print(result, type(result))

result = int(stringer)
print(result, type(result))

result = float(stringer2)
print(result, type(result))

result = int(booler)
print(result, type(result))

result = float(booler2)
print(result, type(result))

result = bool(inter2)
print(result, type(result))

result = str(inter2) + str(floater) + str(booler) + str(booler2)
print(result, type(result))

result = bool(stringer)
print(result, type(result))
