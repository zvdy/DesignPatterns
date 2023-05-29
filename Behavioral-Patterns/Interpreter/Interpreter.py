from abc import ABCMeta, abstractmethod

class AbstractExpression(metaclass=ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes in the
    abstract syntax tree.
    """

    @abstractmethod
    def interpret(self):
        pass


class TerminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with terminal symbols in the
    grammar.
    """

    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with nonterminal symbols in the
    grammar.
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        pass


class Context:
    """
    Contains information that is global to the interpreter.
    """

    def __init__(self):
        self._input = None
        self._output = None


class Client:
    """
    Builds (or is given) an abstract syntax tree representing a particular
    sentence in the language that the grammar defines. The abstract syntax tree
    is assembled from instances of the NonterminalExpression and
    TerminalExpression classes.
    """

    def __init__(self, abstract_syntax_tree):
        self._abstract_syntax_tree = abstract_syntax_tree

    def operation(self):
        self._abstract_syntax_tree.interpret()


def main():
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    client = Client(abstract_syntax_tree)
    client.operation()


if __name__ == "__main__":
    main()