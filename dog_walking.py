
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
        self.is_walking = True

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())
# Parent class


class Dog:

    # Class attribute
    species = 'mammal'
    # Initializer / Instance attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True
        self.is_walking = False
    # instance method

    def description(self):
        return "{} is {}".format(self.name, self.age)

    # instance method
    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

# Child class (inherits from Dog class)


class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)


class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)


my_pets.walk()
