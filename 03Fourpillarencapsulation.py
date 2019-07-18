# Four pillars of OOP
# Encapsulation
# it is considered standard or best practise to keep internal data or attributes
# as private as possible. Only a class should be able to have access to internal variables

# this means a method should be the only way to edit the details, not through object.attribute
# the of using __ is good for preventing accidental change

# to prevent deliberate change we use getters and setters


class Person:

    def __init__(self, age, name, email, height):
        self.age = age
        self.name = name
        self.email = email
        self.set_height(height)  # python calls this variable as _Person__height

    def show_details(self):
        print(f"My name is {self.name} and I am {self.age} years old, my email address is/"
              f" {self.email} my height is {self.__height}")

    def set_height(self, value):
        if value > 9 or value < 0:
            self.__height = 4.5
        else:
            self.__height = value

    def get_height(self):
        return self.__height


markson = Person(25, "Markson", "joe@done.com", 100)

# markson.show_details()
#
# markson.name = "Filipe"

markson.show_details()

markson.set_height(30)  # this cannot change the value, prevents accidental change of a variable, not intentional change

markson.show_details()

print(markson.get_height())
