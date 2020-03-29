# iteration vs recursion - 4000, functions - 4000


result = 0
def mult_iter(a, b):
    """
    Input = int or float
    output = multiplcation of a and b using iteration
    """
    result = 0
    while b > 0:
        result += a
        b -= 1
        print(result)
        print(b)
    return result
    #print(result)
#print(result)
result = mult_iter(5, 5)
print("The final answere is :"+ str(result))


def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)
       
resultR = mult(5, 5)
print("The final recursive answer is: "+ str(resultR))



