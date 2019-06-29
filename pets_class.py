
class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

# Parent class


class Dog:

    # Class attribute
    species = 'mammal'
    # Initializer / Instance attributes

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {}".format(self.name, self.age)

    # instance method
    def eat(self):
        self.is_hungry = False

    # instance method

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

print("I have {} dogs.".format(len(my_pets.dogs)))
for dog in my_pets.dogs:
    dog.eat()
    print("{} is {}".format(dog.name, dog.age))

print("and they're all {}, of course".format(dog.species))
are_my_pets_hungry = False
for dog in my_pets.dogs:
    if dog.is_hungry:
        are_my_pets_hungry = True

if are_my_pets_hungry:
    print("My dogs are hungry")
else:
    print("My dogs are not hungry")
