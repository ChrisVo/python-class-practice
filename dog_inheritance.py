class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class, inherits from Dog Class

class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class, inherits from Dog Class

class BullDog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


jim = BullDog("Chris", 24)


print(jim.run("slowly"))

print(jim.species)
