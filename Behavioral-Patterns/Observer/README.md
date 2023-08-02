# Observer

# Intent

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

# Application

Use the Observer pattern when

* when an abstraction has two aspects, one dependent on the other. Encapsulating these aspects in separate objects lets you vary and reuse them independently.

* when a change to one object requires changing others, and you don't know how many objects need to be changed.

* when an object should be able to notify other objects without making assumptions about who these objects are. In other words, you don't want these objects tightly coupled.

# Diagram

![Observer](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8d/Observer.svg/500px-Observer.svg.png)

# Participants

**Subject**

* knows its observers. Any number of Observer objects may observe a subject.

* provides an interface for attaching and detaching Observer objects.

**Observer**

* defines an updating interface for objects that should be notified of changes in a subject.

**ConcreteSubject**

* stores state of interest to ConcreteObserver objects.

* sends a notification to its observers when its state changes.

**ConcreteObserver**

* maintains a reference to a ConcreteSubject object.

* stores state that should stay consistent with the subject's.

* implements the Observer updating interface to keep its state consistent with the subject's.


# Drawbacks

* Subscribers are notified in random order.

* The update() method of a subscriber should be short, otherwise, the publisher’s notifications will be processed slowly.

* The publisher may send updates that are not relevant to subscribers, forcing them to consume extra time for filtering these messages.

* The publisher and all subscribers must be available at the time of notification. In some cases, it’s impossible to guarantee that.