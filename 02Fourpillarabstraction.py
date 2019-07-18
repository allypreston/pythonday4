# Four pillars of OOP
# Abstraction
# giving the user only the information needed to perform the task
# while keeping unnecessary information hidden
# using python modules as an example of abstraction


class Animal:
    def __init__(self, age, weight, species):
        self.age = age
        self.weight = weight
        self.species = species

    def can_hunt(self, value):
        return value

    def eat(self):
        return "yum yum"

    def sleep(self):
        return "zzzz"

class Mammal(Animal):
    def __init__(self, age, weight, species, name):
        super().__init__(age, weight, species)
        self.name = name

    def speak(self, value):
        return value


class Birds(Animal):
    def __init__(self, age, weight, species, name, feather_colour):
        super().__init__(age, weight, species)
        self.feather_colour = feather_colour

    def can_fly(self, can_fly):
        return can_fly


class Reptile(Animal):
    def __init__(self, age, weight, species, region_found):
        super().__init__(age, weight, species)
        self.region_found = region_found

    def is_venomous(self, value):
        return value