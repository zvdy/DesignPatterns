# Astract Factory

## Intent

Provide an interface for creating families of related or dependent objects without specifying their concrete classes.

## Application

* When a system should be independent of how its products are created, composed, and represented.
* When a system should be configured with one of multiple families of products.
* When a family of related product objects is designed to be used together, and you need to enforce this constraint.
* When you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.
* When the lifetime of the dependency is conceptually shorter than the lifetime of the consumer.
* When you need a run-time value to construct a particular dependency.
* When you want to decide which product to call from a family at run-time.
* When you need to supply one or more parameters only known at run-time before you can resolve a dependency.

## Diagram

![Abstract Factory](https://upload.wikimedia.org/wikipedia/commons/9/9d/Abstract_factory_UML.svg)

## Participants

* **AbstractFactory**
  * declares an interface for operations that create abstract products
* **ConcreteFactory**
    * implements the operations to create concrete product objects
* **AbstractProduct**
    * declares an interface for a type of product object
* **ConcreteProduct**
    * defines a product object to be created by the corresponding concrete factory
    * implements the AbstractProduct interface
* **Client**
    * uses only interfaces declared by AbstractFactory and AbstractProduct classes

## When to use

* a system should be independent of how its products are created, composed, and represented
* a system should be configured with one of multiple families of products
* a family of related product objects is designed to be used together, and you need to enforce this constraint
* you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations
* the lifetime of the dependency is conceptually shorter than the lifetime of the consumer
* you need a run-time value to construct a particular dependency
* you want to decide which product to call from a family at run-time
* you need to supply one or more parameters only known at run-time before you can resolve a dependency

## Benefits

* It isolates concrete classes.
* It makes exchanging product families easy.
* It promotes consistency among products.
* Supporting new kinds of products is difficult.

## Drawbacks

* Supporting new kinds of products is difficult.
* It might be more complex than necessary.
* It can be difficult to provide a common interface for products that don't have a common ancestor.
