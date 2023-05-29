# Bridge

## Intent

Decouple an abstraction from its implementation so that the two can vary independently.

## Applicability

* you want to avoid a permanent binding between an abstraction and its implementation. This might be the case, for example, when the implementation must be selected or switched at run-time.
* both the abstractions and their implementations should be extensible by subclassing. In this case, the Bridge pattern lets you combine the different abstractions and implementations and extend them independently.
* changes in the implementation of an abstraction should have no impact on clients; that is, their code should not have to be recompiled.
* (C++) you want to hide the implementation of an abstraction completely from clients. In C++ the representation of a class is visible in the class interface.

## Diagram

![Bridge](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Bridge_UML_class_diagram.svg/500px-Bridge_UML_class_diagram.svg.png)

## Participants

* **Abstraction**
  * defines the abstraction's interface.
  * maintains a reference to an object of type Implementor.
* **RefinedAbstraction**
    * extends the interface defined by Abstraction.
* **Implementor**
    * defines the interface for implementation classes. This interface doesn't have to correspond exactly to Abstraction's interface; in fact the two interfaces can be quite different. Typically the Implementor interface provides only primitive operations, and Abstraction defines higher-level operations based on these primitives.
* **ConcreteImplementor**
    * implements the Implementor interface and defines its concrete implementation.

## When to use

* you want to avoid a permanent binding between an abstraction and its implementation. This might be the case, for example, when the implementation must be selected or switched at run-time.
* both the abstractions and their implementations should be extensible by subclassing. In this case, the Bridge pattern lets you combine the different abstractions and implementations and extend them independently.
* changes in the implementation of an abstraction should have no impact on clients; that is, their code should not have to be recompiled.
* (C++) you want to hide the implementation of an abstraction completely from clients. In C++ the representation of a class is visible in the class interface.

## Benefits

* It separates the implementation from the interface.
* It improves the extensibility.
* It hides the implementation details from clients.
* It provides the control over the class functionality.
* It comes into picture when we have an abstract class with us and we want to provide its implementation through inheritance.
* It is mostly used in those places where changes are made in the implementation does not affect the client.

## Drawbacks

* It increases the overall code complexity by creating multiple additional classes.
* It can be confusing for the client if you're not using a well-named implementation.