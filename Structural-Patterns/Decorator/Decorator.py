# Decorator

class Component:
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent")


class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        print("ConcreteDecoratorA")


class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        print("ConcreteDecoratorB")


def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)

    concrete_decorator_b.operation()


if __name__ == "__main__":
    main()