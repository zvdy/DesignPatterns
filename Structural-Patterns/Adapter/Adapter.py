class Target:
    """
    Define the domain-specific interface that Client uses.
    """
    def request(self):
        raise NotImplementedError
    
class Adaptee:
    """
    Define an existing interface that needs adapting.
    """
    def specific_request(self):
        return "specific request"
    
class Adapter(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def request(self):
        return self.adaptee.specific_request()
    
def main():
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())

if __name__ == "__main__":
    main()