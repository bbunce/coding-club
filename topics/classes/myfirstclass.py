# define a class
class animal():

    # when the class is created initialise it with the following attributes
    # self refers to the animal class
    # name is a mandatory attribute
    # no_legs is optional and will default to 'None' if not provided
    def __init__(self, name, no_legs=None):
        self.name = name
        self.no_legs = no_legs

    # universal functions (or methods when part of a class) that are part of the animal class
    def move(self):
        print(f'{self.name} wanders about...')

    
    def eat(self):
        print(f'{self.name} eats some food...')


    def sleep(self):
        print(f'{self.name} goes to sleep... ZzzZzzzZzz')


# Instantiate class (create an instance of an object) and initialise the name variable (attribute)
# Initialise class (assigning attribtes to that object as soon as its created)
mypet = animal(name='Felix')
# prints position class instance in memory
print(mypet)
# create a new class instance, it has a different memory position
disney = animal(name='Jerry')
print(disney)
# access class attribute - don't use brackets as its not a method/function
print(mypet.name)
# assign or update attribute
mypet.name = 'Salem'
print(mypet.name)
# assign another attribte
mypet.no_legs = 4
print(mypet.no_legs)
# create a new attribute
mypet.omnivore = True
print(mypet.omnivore)
# these new attributes will only belong to this specific instance
# any new or existing instances of this class will have the default attributes
try:
    print(disney.omnivore)
except AttributeError as e:
    print('this animal class instance doesnt have the omnivore attriute', e)

# use vars and dir functions to findout more about a class
# vars() returns attribtes of an object
print("\nvars() function\n", "-"*20)
print(vars(animal))
print(mypet.__dict__)
# dir() returns properties and methods
print("\ndir() function\n", "-"*20)
print(dir(mypet), '\n\n')

# acces a method
mypet.move()

# inheritance
class dog(animal):
    pass

try:
    mydog = dog()
except TypeError as e:
    print("Dog class inherits same attributes as animal including 'name' which is mandatory.")
    mydog = dog(name='Rex')

mydog.eat()

# inheritance
class cat(animal):
    

    def __init__(self, name, no_legs, breed):
        pass
