class State:
    def doAction(self, context):
        pass

class StartState(State):
    def doAction(self, context):
        print('Player is in start state')
        context.setState(self)

    def toString(self):
        return 'Start State'
    
class StopState(State):
    def doAction(self, context):
        print('Player is in stop state')
        context.setState(self)

    def toString(self):
        return 'Stop State'
    
class Context:
    def __init__(self):
        self.state = None

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state
    
def main():
    context = Context()
    startState = StartState()
    startState.doAction(context)
    print(context.getState().toString())
    stopState = StopState()
    stopState.doAction(context)
    print(context.getState().toString())

if __name__ == '__main__':
    main()