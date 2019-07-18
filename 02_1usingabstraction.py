from PycharmProjects.pythonbasics_engineeringday4.Fourpillarabstraction import Reptiles
class Snake(Reptiles):
    def __init__(self, age, weight, species, region, number_of_fangs, length):
        super().__init__(age, weight, species, region)
        self.number_of_fangs = number_of_fangs
        self.length = length

    def can_constrict(self, bool_value):
        return bool_value

    def can_swim(self, bool_value):
        return bool_value


python = Snake(35, 450, "Pythorus", "Moorgate", 2, 12)
print(python.length)
print(python.species)
print(python.can_constrict(True))
