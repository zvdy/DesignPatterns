# State

# Intent

State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

# Application

Use the State pattern when

* an object's behavior depends on its state, and it must change its behavior at run-time depending on that state,

* operations have large, multipart conditional statements that depend on the object's state. This state is usually represented by one or more enumerated constants. Often, several operations will contain this same conditional structure. The State pattern puts each branch of the conditional in a separate class. This lets you treat the object's state as an object in its own right that can vary independently from other objects.

# Diagram

![State](https://upload.wikimedia.org/wikipedia/commons/e/ec/W3sDesign_State_Design_Pattern_UML.jpg)

# Participants

**Context**

* defines the interface of interest to clients.

* maintains an instance of a ConcreteState subclass that defines the current state.

**State**

* defines an interface for encapsulating the behavior associated with a particular state of the Context.

**ConcreteState subclasses**

* each subclass implements a behavior associated with a state of Context.

# Drawbacks

* Applying the State pattern can be overkill if a state machine has only a few states or rarely changes.

* The State pattern requires creating new classes for each distinct state that an object can be in.

* State-specific behavior is spread across many objects. Without careful design, this can lead to a system that's difficult to understand and maintain.

* The State pattern does not specify where the state transitions will be defined. The choices are two: the Context object, or each individual State subclass. The advantage of the latter option is ease of adding new State subclasses. The disadvantage is each State subclass has knowledge of (coupling to) its siblings, which introduces dependencies between subclasses.

* State objects can be shared.