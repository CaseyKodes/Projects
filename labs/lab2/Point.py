'''The point class creates point objects that have an x and y value and a 
   magnitude that is the distance from the origin
   points are equal when they have the same distance from the origin'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def dist_from_origin(self):
        return (self.x**2+self.y**2)**.5

    def __lt__(self, other):
        magself = self.dist_from_origin()
        magother = other.dist_from_origin()
        return magself<magother

    def __gt__(self, other):
        magself = self.dist_from_origin()
        magother = other.dist_from_origin()
        return magself>magother

    def __eq__(self, other):
        magself = self.dist_from_origin()
        magother = other.dist_from_origin()
        return magself==magother
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
        


# ^^^Implement class and functionality above (remember to include docstrings!)
# vvvImplement tests below

if __name__ == '__main__':
    # All tests should use `assert`, not `print`
    
    ##### test init #####
    # assert correct x
    # assert correct 
    p1 = Point(3, 4)
    assert p1.x == 3
    assert p1.y == 4

    ##### test lt #####
    # Expected True (e.g `p1 < p2`)
    # Expected False (e.g. `not p1 < p2`)
    p1 = Point(5,6)
    p2 = Point(5,12)
    assert p1<p2
    #assert not p1<p2

    ##### test gt #####
    # Expected True (e.g `p1 > p2`)
    # Expected False (e.g. `not p1 > p2`)
    p1 = Point(10,4)
    p2 = Point(5,3)
    assert p1 > p2
    #assert not p1 > p2

    ##### test eq #####
    # Expected True (e.g `p1 == p2`)
    # Expected False (e.g. `not p1 == p2`)
    p1 = Point(5,7)
    p2 = Point(7,5)
    assert p1 == p2
    #assert not p1 == p2

    ##### test str #####
    # assert str(some_point) == expected_string
    p3 = Point(6,9)
    expectedStinrg = "Point (6, 9)"
    assert str(p3) == expectedStinrg

    ##### test dist_from_origin() #####
    p5 = Point(5,12)
    expectedDist = 13 # -> Point.dist_from_origin(p5)
    testDist = p5.dist_from_origin()
    assert testDist == expectedDist
   
print ("we are done")