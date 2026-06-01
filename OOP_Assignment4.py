# Vehicle System using Polymorphism

class Vehicle:
    def start(self):
        print("Vehicle starts")


class Car(Vehicle):
    def start(self):
        print("Car starts with key")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with self-start")


# Creating objects
c1 = Car()
b1 = Bike()

c1.start()
b1.start()
