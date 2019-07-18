# Four pillars of OOP
# Inheritance
# used to allow classes to inherit information from another overarching class


class Vehicle:
    def __init__(self, make, colour, engine_size, year, speed):
        self.make = make
        self.colour = colour
        self.engine_size = engine_size
        self.year = year
        self.speed = speed

    def start(self):
        return "vroom"

    def stop(self):
        return "screech"

    def accelerate(self):
        return self.speed ++ 10


class Truck(Vehicle):
    def __init__(self, make, colour, engine_size, year, trailer_size, speed):
        super().__init__(make, colour, engine_size, year, speed) # does not need self
        self.trailer_size = trailer_size

    def detach_trailer(self):
        return "uncouples"


class Boat(Vehicle):
    def __init__ (self, make, colour, engine_size, year, speed, sail_size, deck_size, rudder_position):
        super().__init__(make, colour, engine_size, year, speed)
        self.sail_size = sail_size
        self.deck_size = deck_size
        self.rudder_position = rudder_position

    def mooring(self):
        return "port to starboard"

    def sinking(self):
        self.speed = 0


my_car = Vehicle("Honda", "Red", 1.6, 1995, 20)
print(f"Daniel has a {my_car.make} of size {my_car.engine_size} of {my_car.colour} and is a {my_car.year} model")
my_truck = Truck("BMW", "white", 7.5, 2003, 14, 10)
print(f"Nathan has a {my_truck.make} of size {my_truck.engine_size} of {my_truck.colour} and is a {my_truck.year}/"
      f" model, it has a {my_truck.trailer_size}ft trailer")

print(my_truck.stop())

my_boat = Boat("pirate ship", "brown", "wind", 1600, 150, 31, 10, "rear left")
print(my_boat.make, my_boat.rudder_position)
my_boat.sinking()
print(my_boat.speed)
