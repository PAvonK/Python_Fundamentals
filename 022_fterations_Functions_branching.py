# Iteration - 2000, Branching - 1000


def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    #result = 0
    #xTemp = 0
  
    fact = 1
    while fact <= x:
        #fact = b
        if (b**fact) > x:
            fact -= 1
            return fact
            break
        elif (b**fact) == x:
            return fact 
            break
        else:
            fact += 1
           
print(myLog(82, 4))     
        
# Correct