# Proxy

# Intent

Provide a surrogate or placeholder for another object to control access to it.

# Application

Use the Proxy pattern when

* there is a need for a more versatile or sophisticated reference to an object than a simple pointer. A proxy can be used to implement smart pointers, which perform additional actions when an object is accessed. For example, a proxy could check to see if an object is locked before it is accessed to ensure that no other object can change it.
* a wrapper is needed to perform additional housekeeping functions when an object is accessed. For example, a proxy could fire an event when an object gets accessed, allowing interested parties to monitor access to it.
* the original object is stored in a location that is inaccessible to the client (e.g., a remote server or a protected data structure such as a lock in an operating system). The proxy acts as a surrogate for the original object, retrieving it, keeping it elsewhere, or creating it on demand.
* an object needs to be created on demand. For example, a proxy could serve as a local representative for an object that resides in another address space. A virtual proxy might create expensive objects on demand (e.g., a page in a book), or it might hide the fact that clients are accessing a preexisting instance.
* a class of pointer-like objects is needed, such as references to remote objects, expensive objects, or protected objects.

# Diagram

![Proxy](https://en.wikipedia.org/wiki/Proxy_pattern#/media/File:Proxy_pattern_diagram.svg)

# Participants

**Proxy**

* maintains a reference that lets the proxy access the real subject. Proxy may refer to a Subject if the RealSubject and Subject interfaces are the same.

* provides an interface identical to Subject's so that a proxy can be substituted for the real subject.

* controls access to the real subject and may be responsible for creating and deleting it.

* other responsibilities depend on the kind of proxy:

  * **remote proxies** are responsible for encoding a request and its arguments and for sending the encoded request to the real subject in a different address space. A remote proxy provides a local representative for an object in a different address space.

  * **virtual proxies** may cache additional information about the real subject so that they can postpone accessing it. For example, the ImageProxy from the Motivation caches the real images's extent. Virtual proxies are also referred to as lazy proxies because they postpone object creation until absolutely necessary.

  * **protection proxies** check that the caller has the access permissions required to perform a request.

**Subject**

* defines the common interface for RealSubject and Proxy so that a Proxy can be used anywhere a RealSubject is expected.

**RealSubject**

* defines the real object that the proxy represents.

# When to use

* a more versatile or sophisticated reference to an object is needed. Use a proxy when the complexity of an object warrants it.

* a simpler or more lightweight representation of the comlex object is needed: the cost of creating and maintaining the complex object is high, and you don't need it right away.

* access to a real object should be controlled: use a proxy when you need "smart" reference. A smart reference is a replacement for a bare pointer that performs additional actions when an object is accessed. Typical uses include

  * counting the number of references to the real object so that it can be freed automatically when there are no more references (also called smart pointers [Ede92]).

  * loading a persistent object into memory when it's first referenced.

  * checking that the real object is locked before it's accessed to ensure that no other object can change it.

# Benefits

* Controlled access to the real object.

* Reduced complexity when the real object is heavy.

* Protected access to the real object.

* The proxy can be made to behave exactly like the real object.

# Drawbacks

* The level of indirection can be high, which complicates the system.

* The client may not be aware of the existence of the proxy.

* The proxy may not do as well as the real subject in terms of efficiency.

# Variants

* **Remote Proxy** provides a local representative for an object in a different address space.

* **Virtual Proxy** creates expensive objects on demand.

* **Protection Proxy** controls access to the original object. Protection proxies are useful when objects should have different access rights.

* **Smart Reference** performs additional actions when an object is accessed. Typical uses include:

  * counting the number of references to the real object so that it can be freed automatically when there are no more references (also called smart pointers [Ede92]).

  * loading a persistent object into memory when it's first referenced.

  * checking that the real object is locked before it's accessed to ensure that no other object can change it.
