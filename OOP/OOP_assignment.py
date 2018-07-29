#Qn1. Fill in the line class methods to accept cordinate as a pair of tuples and return the slope and distance of a line
class Line(object):
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ((x2-1)**2 + (y2-1)**2) ** 0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float ((y2-y1))/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

li.distance()
9.433981132056603 #results

li.slope()
1.6 #results


#Qn2.Fill iin the class  

class Cylinder(object):
    def __init__(self, height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * (3.14) * (self.radius) **2

    def surface_area(self):
        top = (3.14) * (self.radius)**2
        return 2*top + 2*3.14*self.radius*self.height

c = Cylinder(2,3)

c.volume()
56.52 #resuts

c.surface_area()
94.2 #results

