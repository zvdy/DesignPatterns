class Mediator:
    def __init__(self):
        self._colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def distribute(self, sender, message):
        for colleague in self._colleagues:
            if colleague != sender:
                colleague.receive(message)


class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

    def send(self, message):
        self._mediator.distribute(self, message)

    def receive(self, message):
        pass

class ConcreteColleague(Colleague):
    def receive(self, message):
        print(message)

def main():
    mediator = Mediator()
    colleague1 = ConcreteColleague(mediator)
    colleague2 = ConcreteColleague(mediator)
    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)
    colleague1.send('Hello')
    colleague2.send('Goodbye')

if __name__ == '__main__':
    main()
