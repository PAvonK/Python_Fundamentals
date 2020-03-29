# Object Oriented Prorgramming - 9000

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

c = Coordinate(3,4)
origin = Coordinate(0,0)


#print(c.x) prints... 3
#print(origin.x) prints... 0
#print(c.x, c.y, origin.x, origin.y) prints... 3 4 0 0

        