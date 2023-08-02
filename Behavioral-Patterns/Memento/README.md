# Memento

# Intent

Without violating encapsulation, capture and externalize an object's internal state so that the object can be restored to this state later.

# Application

Use the Memento pattern when

* a snapshot of (some portion of) an object's state must be saved so that it can be restored to that state later, and
* a direct interface to obtaining the state would expose implementation details and break the object's encapsulation.

## Diagram

![Memento](https://upload.wikimedia.org/wikipedia/commons/3/38/W3sDesign_Memento_Design_Pattern_UML.jpg)

# Participants

**Memento**

* stores internal state of the Originator object. The memento may store as much or as little of the originator's internal state as necessary at its originator's discretion.

**Originator**

* creates a memento containing a snapshot of its current internal state.

**Caretaker**

* is responsible for the memento's safekeeping.

# Drawbacks

* The cost of creating and maintaining mementos may be prohibitive.
