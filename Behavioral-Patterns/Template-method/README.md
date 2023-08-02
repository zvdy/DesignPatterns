# Tempate Method

# Intent

Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

# Application

Use the Template Method pattern when

* you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.

* you want to make sure that clients don't override the critical steps of an algorithm.

# Diagram

![Template Method](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/W3sDesign_Template_Method_Design_Pattern_UML.jpg/500px-W3sDesign_Template_Method_Design_Pattern_UML.jpg)

# Participants

**AbstractClass**

* defines abstract primitive operations that concrete subclasses define to implement steps of an algorithm.

* implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects.

**ConcreteClass**

* implements the primitive operations to carry out subclass-specific steps of the algorithm.

# Drawbacks

* You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.

* Template methods tend to be harder to maintain the more steps they have.

* The overall complexity of the code increases since you need to introduce a lot of new subclasses to implement the variations of an algorithm.

* The clients must be aware of the concrete classes that implement the template method.

* You might violate the Hollywood Principle by letting high-level classes call low-level classes directly.

* You can overcome some of these drawbacks by applying other creational patterns, such as Factory Method, Builder or Prototype.