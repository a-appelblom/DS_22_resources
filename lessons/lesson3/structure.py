# Först i en fil ska importer ligga.
import random
import enum

# Globala variabler
global x
x = 100

# Funktioner


# main
def main():
    print("My program")
    result = my_function()
    print(result)


# hjälpfunktioner
def my_function():
    # Först ska variabler ligga.
    global x
    # Sen logik
    res = x+1

    # sist return
    return res


main()
