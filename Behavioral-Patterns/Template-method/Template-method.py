class TemplateMethod:
    def __init__(self):
        pass

    def template_method(self):
        self.step_one()
        self.step_two()
        self.step_three()

    def step_one(self):
        print("TemplateMethod.step_one")

    def step_two(self):
        print("TemplateMethod.step_two")

    def step_three(self):
        print("TemplateMethod.step_three")

class ConcreteClassA(TemplateMethod):
    def __init__(self):
        TemplateMethod.__init__(self)

    def step_two(self):
        print("ConcreteClassA.step_two")

class ConcreteClassB(TemplateMethod):
    def __init__(self):
        TemplateMethod.__init__(self)

    def step_three(self):
        print("ConcreteClassB.step_three")

def main():
    concrete_class_a = ConcreteClassA()
    concrete_class_b = ConcreteClassB()
    concrete_class_a.template_method()
    concrete_class_b.template_method()