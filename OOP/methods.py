#functions inside the body of a class
#Used in the encapsulation concept of the OOP paradgm
class Circle(object):

    #class object attribute
    pi =3.14

    def __init__(self, radius = 1):
        self.radius = radius

    def area(self):
        #radius **2 * pi
        return (self.radius **2) * Circle.pi

    def set_radius(self, new_radius):
        """
        This method takes in a radius and resets the current radius of a circle

        """
        self.radius = radius
        

