# Facade

## Intent

Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

## Application

Use the Facade pattern when

* you want to provide a simple interface to a complex subsystem. Subsystems often get more complex as they evolve. Most patterns, when applied, result in more and smaller classes. This makes the subsystem more reusable and easier to customize, but it also becomes harder to use for clients that don't need to customize it. A facade can provide a simple default view of the subsystem that is good enough for most clients. Only clients needing more customizability will need to look beyond the facade.
* there are many dependencies between clients and the implementation classes of an abstraction. Introduce a facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
* you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

## Diagram

![Facade](https://en.wikipedia.org/wiki/Facade_pattern#/media/File:Example_of_Facade_design_pattern_in_UML.png)

## Participants

**Facade**

* knows which subsystem classes are responsible for a request.

* delegates client requests to appropriate subsystem objects.

**Subsystem classes**

* implement subsystem functionality.

* handle work assigned by the Facade object.

* have no knowledge of the facade; that is, they keep no references to it.

## When to use

* you want to provide a simple interface to a complex subsystem. Subsystems often get more complex as they evolve. Most patterns, when applied, result in more and smaller classes. This makes the subsystem more reusable and easier to customize, but it also becomes harder to use for clients that don't need to customize it. A facade can provide a simple default view of the subsystem that is good enough for most clients. Only clients needing more customizability will need to look beyond the facade.
* there are many dependencies between clients and the implementation classes of an abstraction. Introduce a facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
* you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

## Benefits

* A facade reduces the learning curve necessary to successfully leverage the subsystem.

* It promotes weak coupling between the subsystem and its clients.

* It doesn't prevent applications from using subsystem classes if they need to.

## Drawbacks

* A facade can become a god object coupled to all classes of an app.

* A facade can mask a poor design choice, preventing developers from seeing the underlying complexity of the system.

* Clients may have to subclass the facade to make it more convenient to use.