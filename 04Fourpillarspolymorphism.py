# Four pillars of OOP
# polymorphism
# method polymorphism - covered earlier
# ## when a method is behaving differently depending on the data or parameters passed to it
# method overload

# inheritance polymorphism - not covered yet
# ## when a sub class can take the place of its superclass and respond to message call
# method override

class Vehicles:
    def __init__(self, colour, year, make, speed = 0):
        self.colour = colour
        self.year = year
        self.make = make