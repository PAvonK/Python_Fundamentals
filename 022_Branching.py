# branching - 1000, functions - 4000, list operations - 5000

def maxOfThree(a,b,c) :
    """
    a, b, and c are numbers

    returns: the maximum of a, b, and c        
    """
    if a > b:
        bigger = a

    else:
        bigger = b

    if c > bigger:
        bigger = c

    return bigger

print(maxOfThree(2, -10, 100))
print(maxOfThree(7, 9, 10))
print(maxOfThree(6, 1, 5))
print(maxOfThree(0, 40, 20))