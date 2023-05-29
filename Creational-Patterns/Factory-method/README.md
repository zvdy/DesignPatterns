# Factory method

# Intent

Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.

# Application

Use the Factory Method pattern when

* a class can't anticipate the class of objects it must create
* a class wants its subclasses to specify the objects it creates
* classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

# Diagram

![Factory Method](https://upload.wikimedia.org/wikipedia/commons/4/43/W3sDesign_Factory_Method_Design_Pattern_UML.jpg)

# Participants

* **Product**
  * defines the interface of objects the factory method creates
* **ConcreteProduct**
    * implements the Product interface
* **Creator**
    * declares the factory method, which returns an object of type Product. Creator may also define a default implementation of the factory method that returns a default ConcreteProduct object.
    * may call the factory method to create a Product object.
* **ConcreteCreator**
    * overrides the factory method to return an instance of a ConcreteProduct.

# When to use

* a class can't anticipate the class of objects it must create
* a class wants its subclasses to specify the objects it creates
* classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

# Benefits

* It avoids tight coupling between creator and concrete products.
* Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.
* Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.
* You can provide users of the framework with an opportunity to customize the products you provide.
* It lets you add new products to the app without breaking existing client code.

# Drawbacks

* The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.
* The code may be more confusing for the client since you’re hiding the concrete product creation logic from them.