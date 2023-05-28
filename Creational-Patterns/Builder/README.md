# Builder

## Intent

Separate the construction of a complex object from its representation so that the same construction process can create different representations.

## Application

* When the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
* When the construction process must allow different representations for the object that's constructed.

## Diagram

![Builder](https://upload.wikimedia.org/wikipedia/commons/f/f3/Builder_UML_class_diagram.svg)

## Participants

* **Builder**
  * specifies an abstract interface for creating parts of a Product object
* **ConcreteBuilder**
    * constructs and assembles parts of the product by implementing the Builder interface
    * defines and keeps track of the representation it creates
    * provides an interface for retrieving the product
* **Director**
    * constructs an object using the Builder interface
* **Product**
    * represents the complex object under construction
    * includes classes that define the constituent parts, including interfaces for assembling the parts into the final result

## When to use

* the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
* the construction process must allow different representations for the object that's constructed

## Benefits

* It lets you vary a product's internal representation.
* It isolates code for construction and representation.
* It gives you finer control over the construction process.
* It lets you construct complex objects step by step.

## Drawbacks

* It requires creating a separate ConcreteBuilder for each different type of Product.
* It requires the builder classes to be mutable.