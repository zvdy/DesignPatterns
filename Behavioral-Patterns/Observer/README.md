# Observer

# Intent

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

# Application

Observer is pretty common in Java code. It’s a core part of the JDK’s [java.util](https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html) package, and is provided by many other libraries. That’s why it’s crucial to understand this pattern and know how to apply it to real-world systems.

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