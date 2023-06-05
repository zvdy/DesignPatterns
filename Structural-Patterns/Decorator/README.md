# Decorator

## Intent

Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

## Application

Use the Decorator pattern

* to add responsibilities to individual objects dynamically and transparently, that is, without affecting other objects
* for responsibilities that can be withdrawn
* when extension by subclassing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination. Or a class definition may be hidden or otherwise unavailable for subclassing.

## Diagram

![Decorator](https://upload.wikimedia.org/wikipedia/commons/8/83/W3sDesign_Decorator_Design_Pattern_UML.jpg)

## Participants

**Component**

* defines the interface for objects that can have responsibilities added to them dynamically.

**ConcreteComponent**

* defines an object to which additional responsibilities can be attached.

**Decorator**

* maintains a reference to a Component object and defines an interface that conforms to Component's interface.

**ConcreteDecorator**

* adds responsibilities to the component.

## When to use

* to add responsibilities to individual objects dynamically and transparently, that is, without affecting other objects
* for responsibilities that can be withdrawn
* when extension by subclassing is impractical. Sometimes a large number of independent extensions are possible and would produce an explosion of subclasses to support every combination. Or a class definition may be hidden or otherwise unavailable for subclassing.

## Benefits

* More flexibility than static inheritance.
* Avoids feature-laden classes high up in the hierarchy.
* A decorator and its component aren't identical.
* Lots of little objects.

## Drawbacks

* Can complicate the process of instantiating the component.
* Lots of little objects.
