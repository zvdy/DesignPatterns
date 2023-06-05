# Prototype

## Intent

Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.

## Application

Use the Prototype pattern when a system should be independent of how its products are created, composed, and represented; and

* when the classes to instantiate are specified at run-time, for example, by dynamic loading; or
* to avoid building a class hierarchy of factories that parallels the class hierarchy of products; or
* when instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state.

## Diagram

![Prototype](https://en.wikipedia.org/wiki/Prototype_pattern#/media/File:Prototype_UML.svg)

# Participants

* **Prototype**
  * declares an interface for cloning itself
* **ConcretePrototype**
    * implements an operation for cloning itself
* **Client**
    * creates a new object by asking a prototype to clone itself

# When to use

* when a system should be independent of how its products are created, composed, and represented; and
* when the classes to instantiate are specified at run-time, for example, by dynamic loading; or
* to avoid building a class hierarchy of factories that parallels the class hierarchy of products; or
* when instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state.

# Benefits

* Adding and removing products at run-time.
* Specifying new objects by varying values.
* Specifying new objects by varying structure.
* Reduced subclassing.
* Configuring an application with classes dynamically.

# Drawbacks

* Cloning complex objects that have circular references might be very tricky.
* Cloning objects that have references to external resources might be impossible.
