# CW 1/24/23


'''class Vector:
    # constructor method 
    def __init__(self,x,y):
        self.x=x
        self.y=y
        # instance variables

    def magnitiude(self):
        return (self.x**2 + self.y**2)**(1/2)
    
    def __repr__(self):  # print function 
        return f"Vector: {self.x}, {self.y}"
'''

class person:
    def __init__(self,name,netid):
        self.name = name
        self.netid = netid
    
    def __repr__(self):
        return f"Person: {self.name} with netID of {self.netid}"

class Employee(person):
    def __init__(self,name,netid,office):
        # method 1 best method calls direct parent 
        person.__init__(self,name,netid)
        self.office = office

        # method 2 known from java but does not work well in python because of python inheritance tree
        super().__init__(name,netid)

        # method 3 dont do 
        self.name = name
        self.netid = netid
        self.office = office


class shape:

class circle (shape): # inheritance ( a circle IS A shape)

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class cirlce (point):
    def __init__(self,x,y,radius):
        point.__init__(self,x,y)
        self.radius = radius 

class circle:
    def __init__(self,x,y,radius):
        self.center = point(x,y)  # composition (a circle HAS A point)
        self.radius = radius

# polymorphism writing code that does not care about object type 

    