class Person:
    age: int
    name: str
    __spy_name: str

    def __init__(self, name: str, age: int, spy_name: str):
        self.name = name
        self.age = age
        self.__spy_name = spy_name

    def get_spy_name(self):
        return self.__spy_name

    def set_spy_name(self, spy_name: str):
        self.__spy_name = spy_name

    def __shoutout_spy_name(self):
        print(self.__spy_name.upper())

    def let_it_out_shoutout(self):
        self.__shoutout_spy_name()


anton = Person("Anton", 30, "Beardboy")

# anton.name = "Evert"
# anton.__spy_name = "Weirdboy"

print(anton.name)
# print(anton.__spy_name)
print(anton.get_spy_name())
anton.set_spy_name("HeyBoy")
print(anton.get_spy_name())

# anton.__shoutout_spy_name()
anton.let_it_out_shoutout()
