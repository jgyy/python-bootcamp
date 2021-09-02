"""
71. Object Oriented Programming - Inheritance and Polymorphism
"""


class Animal:
    """
    Animal class
    """

    def __init__(self, name):
        self.name = name
        print("ANIMAL CREATED")

    def who_am_i(self):
        """
        method within a class
        """
        print("I am a animal", self)

    def eat(self):
        """
        method within a class
        """
        print("I am eating", self)

    def speak(self):
        """
        method within a class
        """
        print(self)
        raise NotImplementedError("Subclass must implement this abstract method.")


class Dog(Animal):
    """
    Animal class
    """

    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name
        print("Dog Created")

    def bark(self):
        """
        method within a class
        """
        print("WOOF!", self)

    def speak(self):
        """
        method within a class
        """
        return self.name + " says woof!"


class Cat(Animal):
    """
    Animal class
    """

    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("Niko")
niko.bark()
felix = Cat("Felix")
for pet in (niko, felix):
    print(type(pet))
    print(pet.name)
    print(pet.speak())
    pet.who_am_i()
    pet.eat()
