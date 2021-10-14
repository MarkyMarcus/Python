class Animal:
    legs = 0
    fur = False

    def type(self):
        print("I am some type of animal")

class Pet(Animal):
    def speak(self):
        pass

class Cat(Pet):
    legs = 4
    fur = True
    def type(self):
        print("I'm a cat")

    def speak(self):
        print('Meow!')

class Dog(Pet):
    legs = 4
    fur = True
    def type(self):
        print("I'm a dog")

    def speak(self):
        print('Bark!')

class Bird(Pet):
    legs = 2
    def type(self):
        print("I'm a bird")

    def speak(self):
        print('Chirp!')

# TODO: Create a new class of pet
class Snake(Pet):
    def type(self):
        print("I'm a snake")

pets = []
# TODO: Create instances of 3 or more pets and add them to the pets list
pets.append(Cat())
pets.append(Dog())
pets.append(Bird())
pets.append(Snake())

for pet in pets:
    print('*'*50)
    pet.type()
    pet.speak()
    print('I have %d legs' % pet.legs)
    if pet.fur:
        print('I have fur')
    else:
        print('I do not have fur')
