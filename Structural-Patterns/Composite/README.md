# Composite

## Intent

Compose objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.

## Applicability

Use the Composite pattern when

* you want to represent part-whole hierarchies of objects
* you want clients to be able to ignore the difference between compositions of objects and individual objects. Clients will treat all objects in the composite structure uniformly

## Diagram

![Composite](https://upload.wikimedia.org/wikipedia/commons/6/65/W3sDesign_Composite_Design_Pattern_UML.jpg)

## Participants

* **Component**
  * declares the interface for objects in the composition.
  * implements default behavior for the interface common to all classes, as appropriate.
  * declares an interface for accessing and managing its child components.
  * (optional) defines an interface for accessing a component's parent in the recursive structure, and implements it if that's appropriate.
* **Leaf**
    * represents leaf objects in the composition. A leaf has no children.
    * defines behavior for primitive objects in the composition.
* **Composite**
    * defines behavior for components having children.
    * stores child components.
    * implements child-related operations in the Component interface.
* **Client**
    * manipulates objects in the composition through the Component interface.

## When to use

* you want to represent part-whole hierarchies of objects
* you want clients to be able to ignore the difference between compositions of objects and individual objects. Clients will treat all objects in the composite structure uniformly

## Benefits

* It defines class hierarchies that contain primitive and complex objects.
* It makes easier to you to add new kinds of components.
* It provides flexibility of structure with manageable class or interface.

## Drawbacks

* It makes the design overly general. It makes harder to restrict the components of a composite.
* It makes harder to restrict the components of a composite.
* It makes your design overly general.