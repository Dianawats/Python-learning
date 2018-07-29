class Animal(object):   #Animal is the base class
    def __init__(self):
        print "Animal created"
    
    def whoAmI(self):
        print "Dog"

    def eat(self):
        print "Eating"

#Derrived class modify the existing behaviour of the base class, 
#it was modified by overriding using the whoAmI method with in the dog class
class Dog(Animal):  #Dog is inheriting from animal, Dog is the derrived class. It inherits the functionality of the base class
    def __init__(self):
        Animal.__init__(self)
        print "Dog created"

    def whoAmI(self):
        print "Dog"

    def bark(self):
        print "whoof!"

    d = Dog()
    #results
    Animal created
    Dog created

    d.whoAmI()
    Dog #results

    d.eat()
    Eating #results

    d.bark()
    whoof! #results
