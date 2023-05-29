# Interpreter

The Interpreter pattern offers a scripting language that allows end-users to customize their solution. The Interpreter pattern is a design pattern that specifies how to evaluate sentences in a language. The basic idea is to have a class for each symbol (terminal or nonterminal) in a specialized computer language. The syntax tree of a sentence in the language is an instance of the composite pattern and is used to evaluate (interpret) the sentence for a client.

## Intent

Given a language, define a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.

## Application

* When you want to interpret a DSL.
* When you want to implement a simple grammar.
* When you want to implement a simple grammar to represent a simple problem domain.

## Diagram

![Interpreter](https://upload.wikimedia.org/wikipedia/commons/b/bf/Interpreter_Design_Pattern_Diagram.png)

## Participants

* **AbstractExpression**
    * declares an abstract Interpret operation that is common to all nodes in the abstract syntax tree
* **TerminalExpression**
    * implements an Interpret operation associated with terminal symbols in the grammar
    * an instance is required for every terminal symbol in a sentence
* **NonterminalExpression**
    * one such class is required for every rule R ::= R1R2...Rn in the grammar
    * maintains instance variables of type AbstractExpression for each of the symbols R1 through Rn
    * implements an Interpret operation for nonterminal symbols in the grammar. Interpret typically calls itself recursively on the variables representing R1 through Rn
* **Context**
    * contains information that is global to the interpreter
* **Client**
    * builds (or is given) an abstract syntax tree representing a particular sentence in the language that the grammar defines. The abstract syntax tree is assembled from instances of the NonterminalExpression and TerminalExpression classes
    * invokes the Interpret operation

## When to use

* When you want to interpret a DSL.
* When you want to implement a simple grammar.
* When you want to implement a simple grammar to represent a simple problem domain.

## Benefits

* It's easy to change and extend the grammar.
* Implementing the grammar is easy, too.
* Adding new ways to interpret expressions is easy.

## Drawbacks

* Complex grammars are hard to maintain.
* Complex grammars are hard to implement.
* Adding new ways to interpret expressions is hard.