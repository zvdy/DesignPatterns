# Flyweight

## Intent

Use sharing to support large numbers of fine-grained objects efficiently.

## Application

Use the Flyweight pattern when

* an application uses a large number of objects
* storage costs are high because of the sheer quantity of objects
* most object state can be made extrinsic
* many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed
* the application doesn't depend on object identity. Since flyweight objects may be shared, identity tests will return true for conceptually distinct objects.

## Diagram

![Flyweight](https://upload.wikimedia.org/wikipedia/commons/4/4e/W3sDesign_Flyweight_Design_Pattern_UML.jpg)

## Participants


**Flyweight**

* declares an interface through which flyweights can receive and act on extrinsic state.

**ConcreteFlyweight**

* implements the Flyweight interface and adds storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable. Any state it stores must be intrinsic, that is, it must be independent of the ConcreteFlyweight object's context.

**UnsharedConcreteFlyweight**

* not all Flyweight subclasses need to be shared. The Flyweight interface enables sharing, but it doesn't enforce it. It is common for UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as children at some level in the flyweight object structure (as the Row and Column classes have).

**FlyweightFactory**

* creates and manages flyweight objects

* ensures that flyweight are shared properly. When a client requests a flyweight, the FlyweightFactory object supplies an existing instance or creates one, if none exists.

**Client**

* maintains a reference to flyweight(s).

* computes or stores the extrinsic state of flyweight(s).

## When to use

* an application uses a large number of objects
* storage costs are high because of the sheer quantity of objects
* most object state can be made extrinsic
* many groups of objects may be replaced by relatively few shared objects once extrinsic state is removed
* the application doesn't depend on object identity. Since flyweight objects may be shared, identity tests will return true for conceptually distinct objects.

## Benefits

* Saves memory
* Saves time
* Simplifies code

## Drawbacks

* Increases overall complexity of the code
* Increases run-time costs by trading memory for computation cycles
* Exposes clients to implementation details they shouldn't know about
