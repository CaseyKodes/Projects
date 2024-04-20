#Animals.py

class Animal():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} says something"
    
    def reply(self):
        return self.speak()

class Mammal(Animal):
    pass

class Cat(Mammal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Mammal):
    def speak(self):
        return f"{self.name} says bark"

class Primate(Mammal):
    def speak(self):
        return f"{self.name} says Hello there"

class ComputerScientist(Primate):
    pass
    
if __name__ == '__main__':
    expectedc = "cat says meow"
    expectedd = "dog says bark"
    expectedp = "monkey says Hello there"
    expectedcs = "casey says Hello there"
    expectedcr = "cat says meow"

    c = Cat("cat")
    d = Dog("dog")
    p = Primate("monkey")
    cs = ComputerScientist("casey")

    assert (expectedc == c.speak())
    assert (expectedd == d.speak())
    assert (expectedp == p.speak())
    assert (expectedcs == cs.speak())
    assert (expectedcr == c.reply())

    print("we did it")
