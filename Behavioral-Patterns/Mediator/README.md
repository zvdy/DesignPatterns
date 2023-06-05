# Mediator

# Intent

Define an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.

# Application

Use the Mediator pattern when

* a set of objects communicate in well-defined but complex ways. The resulting interdependencies are unstructured and difficult to understand.
* reusing an object is difficult because it refers to and communicates with many other objects.
* a behavior that's distributed between several classes should be customizable without a lot of subclassing.

# Diagram

![Mediator](https://upload.wikimedia.org/wikipedia/commons/9/92/W3sDesign_Mediator_Design_Pattern_UML.jpg)

# Participants

**Mediator**
* defines an interface for communicating with Colleague objects.

**ConcreteMediator**
* implements cooperative behavior by coordinating Colleague objects.
* knows and maintains its colleagues.

**Colleague classes**
* each Colleague class knows its Mediator object.
* each colleague communicates with its mediator whenever it would have otherwise communicated with another colleague.

# When to use

* a set of objects communicate in well-defined but complex ways. The resulting interdependencies are unstructured and difficult to understand.
* reusing an object is difficult because it refers to and communicates with many other objects.
* a behavior that's distributed between several classes should be customizable without a lot of subclassing.

# Benefits

* It limits subclassing. A mediator localizes behavior that otherwise would be distributed among several objects. Changing this behavior requires subclassing Mediator only; Colleague classes can be reused as is.
* It decouples colleagues. A mediator promotes loose coupling between colleagues. You can vary and reuse Colleague and Mediator classes independently.
* It simplifies object protocols. A mediator replaces many-to-many interactions with one-to-many interactions between the mediator and its colleagues. One-to-many relationships are easier to understand, maintain, and extend.
* It abstracts how objects cooperate. Making mediation an independent concept and encapsulating it in an object lets you focus on how objects interact apart from their individual behavior. That can help clarify how objects interact in a system.

# Drawbacks

* Mediators can become bottlenecks, resulting in a system that's hard to maintain by being overburdened with logic.
* It can be difficult to reuse a mediator object in another system, because mediator objects often have intimate knowledge of their colleagues.
* On the other hand, it might be too general, making it harder to reuse in unrelated systems.