# Singleton

## Intent

Ensure a class only has one instance, and provide a global point of access to it.

## Application

Use the Singleton pattern when

* there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point
* when the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code

## Diagram

![Singleton](https://upload.wikimedia.org/wikipedia/commons/d/dc/Singleton_pattern_uml.png)

## Participants

**Singleton**

* defines an Instance operation that lets clients access its unique instance. Instance is a class operation (that is, a class method in Smalltalk and a static member function in C++).

## When to use

* there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point
* when the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code

## Benefits

* Controlled access to sole instance.
* Reduced name space.
* Permits refinement of operations and representation.
* Permits a variable number of instances.
* More flexible than class operations.

## Drawbacks

* Violates Single Responsibility Principle.
* May be difficult to test.
* May be difficult to subclass if the Singleton class is defined as a final class.