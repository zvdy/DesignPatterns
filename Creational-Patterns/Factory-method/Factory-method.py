from abc import ABCMeta, abstractmethod


class Creator(metaclass=ABCMeta):
    """
    Declare the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory method
    that returns a default ConcreteProduct object.
    Call the factory method to create a Product object.
    """

    def __init__(self):
        self.product = self._factory_method()

    @abstractmethod
    def _factory_method(self):
        pass

    def some_operation(self):
        self.product.interface()


class ConcreteCreator1(Creator):
    """
    Override the factory method to return an instance of a ConcreteProduct1.
    """

    def _factory_method(self):
        return ConcreteProduct1()
    

class ConcreteCreator2(Creator):
    """
    Override the factory method to return an instance of a ConcreteProduct2.
    """

    def _factory_method(self):
        return ConcreteProduct2()
    

class Product(metaclass=ABCMeta):
    """
    Define the interface of objects the factory method creates.
    """

    @abstractmethod
    def interface(self):
        pass


class ConcreteProduct1(Product):
    """
    Implement the Product interface.
    """

    def interface(self):
        print("ConcreteProduct1")


class ConcreteProduct2(Product):
    """
    Implement the Product interface.
    """

    def interface(self):
        print("ConcreteProduct2")


def main():
    concrete_creator_1 = ConcreteCreator1()
    concrete_creator_1.some_operation()

    concrete_creator_2 = ConcreteCreator2()
    concrete_creator_2.some_operation()


if __name__ == "__main__":
    main()