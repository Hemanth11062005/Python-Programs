from abc import ABC, abstractmethod

class Vechicle(ABC):
    @abstractmethod
    def go(self):
        pass
    def stop(self):
        pass

class Car(Vechicle):
    def go(self):
        print("You drive a car")
    def stop(self):
        print("This car is stopped")

class Motorcycle(Vechicle):
    def go(self):
        print("You ride a motorcycle")
    def stop(self):
        print("This motorcycle is stopped")

car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()

car.stop()
motorcycle.stop()