from abc import ABCMeta, abstractmethod

class Command(metaclass=ABCMeta):
    """
    Declare an interface for executing an operation.
    """

    @abstractmethod
    def execute(self):
        pass

class ConcreteCommand(Command):
    """
    Define a binding between a Receiver object and an action.
    Implement Execute by invoking the corresponding operation(s) on Receiver.
    """

    def __init__(self, receiver):
        self._receiver = receiver

    def execute(self):
        self._receiver.action()

class Receiver:
    """
    Know how to perform the operations associated with carrying out a request.
    Any class may serve as a Receiver.
    """

    def action(self):
        pass

class Invoker:
    """
    Ask the command to carry out the request.
    """

    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self):
        self._command.execute()

def main():
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.set_command(command)
    invoker.execute_command()

if __name__ == "__main__":
    main()