# Adapter

## Intent

Convert the interface of a class into another interface clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

## Application

* When you want to use an existing class, and its interface does not match the one you need.
* When you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.
* When you want to increase transparency of classes by not exposing complex or system-specific data structures.
* When you want to reuse legacy code in a new system.
* When you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.
* When you want to use several existing subclasses, but it's impractical to adapt their interface by subclassing every one. An object adapter can adapt the interface of its parent class.

## Diagram

![Adapter](https://upload.wikimedia.org/wikipedia/commons/3/35/ClassAdapter.png)

## Participants

* **Target**
  * defines the domain-specific interface that Client uses.
* **Client**
    * collaborates with objects conforming to the Target interface.
* **Adaptee**
    * defines an existing interface that needs adapting.
* **Adapter**
    * adapts the interface of Adaptee to the Target interface.

## When to use

* you want to use an existing class, and its interface does not match the one you need.
* you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.
* you want to increase transparency of classes by not exposing complex or system-specific data structures.
* you want to reuse legacy code in a new system.
* you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don't necessarily have compatible interfaces.

## Benefits

* It lets you reuse existing classes that may not implement an interface you need.
* It lets you create a reusable class that cooperates with unrelated or unforeseen classes with incompatible interfaces.
* It lets you create a reusable class that cooperates with unrelated or unforeseen classes with incompatible interfaces.
* It lets you create a reusable class that cooperates with unrelated or unforeseen classes with incompatible interfaces.

## Drawbacks

* It can complicate the code if you overuse it. Use it when the benefits are greater than the drawbacks.
* It can complicate the code if you overuse it. Use it when the benefits are greater than the drawbacks.
* It can complicate the code if you overuse it. Use it when the benefits are greater than the drawbacks.
* It can complicate the code if you overuse it. Use it when the benefits are greater than the drawbacks.
