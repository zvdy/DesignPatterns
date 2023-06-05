# Flyweight

import random
import string

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}
    
    def getFlyweight(self, key):
        try:
            flyweight = self.flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self.flyweights[key] = flyweight
        return flyweight
    
    def listFlyweights(self):
        count = len(self.flyweights)
        print(f"FlyweightFactory: I have {count} Flyweights:")
        print("\n".join(map(str, self.flyweights.keys())), end="")


class Flyweight:
    def operation(self, extrinsic_state):
        pass

class ConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"ConcreteFlyweight: {extrinsic_state}")

class UnsharedConcreteFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print(f"UnsharedConcreteFlyweight: {extrinsic_state}")

def addCarToPoliceDatabase(factory, plates, owner, brand, model, color):
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.getFlyweight([brand, model, color])
    flyweight.operation([plates, owner])

def main():
    factory = FlyweightFactory()
    print("Client: Adding a shared flyweight.")
    shared_flyweight = factory.getFlyweight(["Chevrolet", "Camaro2018", "pink"])
    factory.listFlyweights()
    addCarToPoliceDatabase(factory, "CL234IR", "James Doe", "Chevrolet", "Camaro2018", "pink")
    addCarToPoliceDatabase(factory, "CL234IR", "James Doe", "Chevrolet", "Camaro2018", "pink")
    print("\n")
    factory.listFlyweights()


if __name__ == "__main__":
    main()