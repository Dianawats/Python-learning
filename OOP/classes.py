#user defined objects are created using class keyword
#A class is a blueprint that defines the nature of a future object
#from class we construct instances 
#An instance is a specific object created from a particular class
#In class we put in attribute and the method
#An attribute is a characteristic of an object
#A method is an operation we can perform with objects
Class Dog(object):

    #class object attribute
    species = 'Mammal'
    def __init__(self,breed, name):
        self.breed = breed
        self.name = name

sam = Dog(breed= 'Lab')
frank = Dog(breed = 'Huskie', name = 'Sammy')
#results sam.breed, Lab

sam.species #results mammal
sam.name #sammy
