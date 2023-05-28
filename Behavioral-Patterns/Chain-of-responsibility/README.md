# Chain of Responsability

## Application
* When you want to give more than one object the opportunity to handle a request, and you don't want to specify the receiver explicitly.
* When you want to issue a request to one of several objects without specifying the receiver explicitly.
* When the set of objects that can handle a request should be specified dynamically.

## Diagram
![Chain of Responsability](https://upload.wikimedia.org/wikipedia/commons/6/6a/W3sDesign_Chain_of_Responsibility_Design_Pattern_UML.jpg)

## Participants
* **Handler**
  * defines an interface for handling requests
  * (optional) implements the successor link
* **ConcreteHandler**
    * handles requests it is responsible for
    * can access its successor
    * if the ConcreteHandler can handle the request, it does so; otherwise it forwards the request to its successor
* **Client**
    * initiates the request to a ConcreteHandler object on the chain

## When to use
* more than one object may handle a request, and the handler isn't known a priori. The handler should be ascertained automatically
* you want to issue a request to one of several objects without specifying the receiver explicitly
* the set of objects that can handle a request should be specified dynamically

## Benefits
* reduced coupling
* added flexibility in assigning responsibilities to objects
* receipt isn't guaranteed

## Drawbacks
* handling a request can be delayed
* no guarantee that it'll be handled

## Example
* [Wikipedia](https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern#Java)
* [sourcemaking.com](https://sourcemaking.com/design_patterns/chain_of_responsibility)
* [Refactoring Guru](https://refactoring.guru/design-patterns/chain-of-responsibility/python/example)
