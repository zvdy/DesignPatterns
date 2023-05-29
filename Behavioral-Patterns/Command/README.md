# Command

## Intent

Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.

## Application

* Parameterize objects by an action to perform.
* Specify, queue, and execute requests at different times.
* Support undo.
* Support logging changes so that they can be reapplied in case of a system crash.
* Structure a system around high-level operations built on primitive operations.
* Support undo and redo.

## Diagram

![Command](https://upload.wikimedia.org/wikipedia/commons/b/bf/Command_pattern.svg)

## Participants

* **Command**
  * declares an interface for executing an operation
* **ConcreteCommand**
    * defines a binding between a Receiver object and an action
    * implements Execute by invoking the corresponding operation(s) on Receiver
* **Client**
    * creates a ConcreteCommand object and sets its receiver
* **Invoker**
    * asks the command to carry out the request
* **Receiver**
    * knows how to perform the operations associated with carrying out a request

## When to use

* parameterize objects by an action to perform.
* specify, queue, and execute requests at different times.
* support undo.
* support logging changes so that they can be reapplied in case of a system crash.
* structure a system around high-level operations built on primitive operations.
* support undo and redo.

## Benefits

* It decouples the object that invokes the operation from the one that knows how to perform it.
* It allows you to create a sequence of commands by providing a queue system.
* It allows you to implement undo and redo functionality.
* It allows you to implement deferred execution of operations.
* It allows you to assemble a set of simple commands into a complex one.

## Drawbacks

* It increases the overall code complexity by creating multiple additional classes.
* It can be confusing for the client if you're not using a well-named implementation.
