# functions - 4000

def is_even( i ):
    """
    Input: i, is a positive int
    Returns: True if i is even, otherwise False
    """
    print("hi")
    return i%2 == 0

is_even(2*5+25)


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2
   
print(f(4,6))


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a * (x**2) + b * x + c


print(evalQuadratic(3, 6, 2, 9))


def a(x):
   '''
   x: int or float.
   '''
   return x + 1

print(a(a(a(6))))


def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2 
   
f

def a(x, y, z):
     if x:
         return y
     else:
         return z
     
print(a(False, 2, 3))


def a(x, y, z):
     if x:
         return y
     else:
         return z

def b(q, r):
    return a(q>r, q, r)

print(a(3>2, a, b))