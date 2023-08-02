# Visitor

# Intent

Visitor is a behavioral design pattern that lets you separate algorithms from the objects on which they operate.

# Application

Use the Visitor pattern when

* an object structure contains many classes of objects with differing interfaces, and you want to perform operations on these objects that depend on their concrete classes.

* many distinct and unrelated operations need to be performed on objects in an object structure, and you want to avoid "polluting" their classes with these operations. Visitor lets you keep related operations together by defining them in one class. When the object structure is shared by many applications, use Visitor to put operations in just those applications that need them.

* the classes defining the object structure rarely change, but you often want to define new operations over the structure. Changing the object structure classes requires redefining the interface to all visitors, which is potentially costly. If the object structure classes change often, then it's probably better to define the operations in those classes.

# Diagram

![Visitor](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/VisitorDiagram.svg/500px-VisitorDiagram.svg.png)

# Participants

**Visitor**

* declares a Visit operation for each class of ConcreteElement in the object structure. The operation's name and signature identifies the class that sends the Visit request to the visitor. That lets the visitor determine the concrete class of the element being visited. Then the visitor can access the elements directly through its particular interface.

* implements each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding class or object in the structure. ConcreteVisitor provides the context for the algorithm and stores its local state. This state often accumulates results during the traversal of the structure.

**ConcreteVisitor**

* implements each operation declared by Visitor. Each operation implements a fragment of the algorithm defined for the corresponding class or object in the structure. ConcreteVisitor provides the context for the algorithm and stores its local state. This state often accumulates results during the traversal of the structure.

**Element**

* defines an Accept operation that takes a visitor as an argument.

**ConcreteElement**

* implements an Accept operation that takes a visitor as an argument.

**ObjectStructure**

* can enumerate its elements.

* may provide a high-level interface to allow the visitor to visit its elements.

* may either be a Composite (pattern) or a collection such as a list or a set.

# Drawbacks

* Adding new ConcreteElement classes is hard, because Visitor supports only a fixed set of behaviors, and the interface doesn't allow adding new behaviors.

* Visiting all elements of an object structure is hard, because the interface doesn't provide a way to iterate over the elements.

* Accumulating state information is hard, because the interface doesn't provide a way to store values.

* Breaking encapsulation is hard, because the interface gives visitors direct access to the state of the elements.

* Creating a new ConcreteVisitor is hard, because the interface exposes details of the elements.

* The pattern can lead to a system that's difficult to change when new ConcreteElement classes are added frequently. Each new class requires changing the interface and implementation of every visitor. If the visit operation is instead added to the ConcreteElement class, there's no need to change any visitor when adding new ConcreteElement classes.

* The pattern can result in a system with a large number of ConcreteVisitor classes. That makes it harder to understand the system, because behavior isn't localized in one class.

* The pattern requires that the ConcreteElement interface redefines the accept operation in such a way that it dispatches to the right overloaded visitor function. If the language doesn't support overloading, then the element interface will have to provide a separate operation for each ConcreteVisitor. That makes it hard to add new ConcreteVisitor classes to the system.

* The ConcreteElement interface must expose enough information to let visitors do their job. As a result, ConcreteElement classes may have to provide operations that give visitors access to their internal state. This may violate the encapsulation of the elements.

* The pattern makes it hard to add new subclasses of Element. Each new subclass requires a corresponding new operation in every visitor. If the visit operation is instead added to the Element class, there's no need to change any visitor when adding new Element subclasses.



