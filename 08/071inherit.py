class Animal:
    def __init__(self, name):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am a animal")

    def eat(self):
        print("I am eating")

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method.")


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.name = name
        print("Dog Created")

    def bark(self):
        print("WOOF!")

    def speak(self):
        return self.name + " says woof!"


class Cat(Animal):
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
