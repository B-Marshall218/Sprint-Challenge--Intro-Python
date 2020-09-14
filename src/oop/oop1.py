# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

class Vehicle:  # base class
    pass


class GroundVehicle(Vehicle):
    pass


class Car(GroundVehicle):
    pass


class Motorcycle(GroundVehicle):
    pass


class FlightVehicle:  # This is the base class
    pass


class Airplane(FlightVehicle):
    pass


class Starship:  # This is a base class
    pass
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
