# Object Oriented Prorgramming - 9000 (Methods)


#class Weird(object):
#    def __init__(self, x, y):
#        self.y = y
#        self.x = x
#    def getX(self):
#        return x
#    def getY(self):
#        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y

X = 7
Y = 8

#w1 = Weird(X, Y)
#print(w1.getX())
##Type = NoneType
##Output = error
##
#print(w1.getY())
#Type = NoneType
#Output = error
w2 = Wild(X, Y)
#
print(w2.getX())
#Type = int
#Output = 7
#
print(w2.getY())
#Type = int
#Output = 8
#
w3 = Wild(17, 18)
print(w3.getX())
#Type = int
#Output = 17
#
print(w3.getY())
#Type = int
#Output = 18
#
w4 = Wild(X, 18)
print(w4.getX())
#Type = int
#Output = 7
#
print(w4.getY())
#Type = int
#Output = 18
#
X = w4.getX() + w3.getX() + w2.getX()
print(X)
#Type = int
#Output = 31
#
print(w4.getX())
#Type = int
#Output = 7
#
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)
#Type = int
#Output = 44
#
print(w2.getY())
#Type = int
#Output = 8
