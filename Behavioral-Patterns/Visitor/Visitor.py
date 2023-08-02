class Visitor:
    def visit(self, element):
        pass

class ComputerPart:
    def accept(self, visitor):
        pass

class Keyboard(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

class Monitor(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

class Mouse(ComputerPart):
    def accept(self, visitor):
        visitor.visit(self)

class Computer(ComputerPart):
    def __init__(self):
        self.parts = [Mouse(), Keyboard(), Monitor()]

    def accept(self, visitor):
        for part in self.parts:
            part.accept(visitor)
        visitor.visit(self)

class ComputerPartDisplayVisitor(Visitor):
    def visit(self, element):
        if isinstance(element, Computer):
            print('Displaying Computer.')
        elif isinstance(element, Mouse):
            print('Displaying Mouse.')
        elif isinstance(element, Keyboard):
            print('Displaying Keyboard.')
        elif isinstance(element, Monitor):
            print('Displaying Monitor.')

def main():
    computer = Computer()
    computer.accept(ComputerPartDisplayVisitor())