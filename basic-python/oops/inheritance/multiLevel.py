# Base Class
class Vehicle:
    def start(self):
        return "Vehicle started"

# Derived Class
class Car(Vehicle):
    def drive(self):
        return "Car is driving"

# Another Derived Class
class SportsCar(Car):
    def turbo(self):
        return "Turbo mode activated"

# Creating an object of the SportsCar class
sports_car = SportsCar()
print(sports_car.start())   # Inherited from Vehicle
print(sports_car.drive())   # Inherited from Car
print(sports_car.turbo())   # Defined in SportsCar
