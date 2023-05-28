"Builder"

from abc import ABCMeta, abstractmethod

class Builder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def buildPartA(self):
        pass

    @abstractmethod
    def buildPartB(self):
        pass

    @abstractmethod
    def getResult(self):
        pass

class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def buildPartA(self):
        self.product.add("PartA")

    def buildPartB(self):
        self.product.add("PartB")

    def getResult(self):
        return self.product
    
class Product(object):
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product Parts: "),
        for part in self.parts:
            print(part),
        print

class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.buildPartA()
        self.builder.buildPartB()

if __name__ == "__main__":
    builder1 = ConcreteBuilder1()
    director = Director(builder1)
    director.construct()
    product = builder1.getResult()
    product.show()

"""
How to add new product?
1. Create a new class that inherits from Builder
2. Implement the abstract methods

How to add new part?
1. Add a new method in Builder
2. Implement the method in ConcreteBuilder
3. Call the method in Director

Example:
class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def buildPartA(self):
        self.product.add("PartX")

    def buildPartB(self):
        self.product.add("PartY")

    def getResult(self):
        return self.product

class Director(object):
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.buildPartA()
        self.builder.buildPartB()

if __name__ == "__main__":
    builder2 = ConcreteBuilder2()
    director = Director(builder2)
    director.construct()
    product = builder2.getResult()
    product.show()
"""
