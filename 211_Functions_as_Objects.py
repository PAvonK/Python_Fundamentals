# functions as objects - 5000 (fibonacci), recursion - 5000

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2) # function defined to calculate Fibonacci (Hidden currently)

print("*** Wk 3.5 Video 5 Functions as Objects ***")
print()
print("*** applyToEach Exercise ***")
print("*** Applying functions to each element of a list ***")

def applyToEach(L, f):
    """
    assumes L is a list, f a functions mutates
    L by replaving each element, e, of L by f(e)
    """
    for i in range(len(L)): # loops through the entire list and then ...
        L[i] = f(L[i])      # ... applies the called function to each part of list

L = [1, 5, -10, 2.5, 4.7]   # defines the list
applyToEach(L, abs)         # applies built in abs function to each of them
print(L)                    # returns = [1, 5, 10, 2.5, 4.7]

L = [1, 5, -10, 2.5, 4.7]   # defines the list
applyToEach(L, round)       # applies built in round function to each of them
print(L)                    # returns = [1, 5, -10, 2, 5]

L = [1, 5, 20, 14, 3]       # defines the list
applyToEach(L, fib)         # takes the applyToEach function and does the ...
print (L)                   # ... Fibonacci sequence to them.  takes the ...
                            # ... function from the defined function above...
                            # ... returns = [1, 8, 10946, 610, 3]

print()                            
print("*** applyFuns Exercise ***")
print("*** Applying a list of functions to an element ***")

def applyFuns(L, x):        # Function with L for list and x for variable
    for f in L:             # lops through using a for loop
        print(f(x))         # then simply prints thre result of the function...
                            # ... applied to looping variable
        
applyFuns([abs, int, fib], 7)   # This calls the function and uses the list...
                                # ... of abs, int and fib to apply to 7 which ...
                                # ... is x
                                # prints 7(for abs), 7(for int), and 21(for fib)

print()
print("*** General HOP = simple map ***")

for elt in map(abs, [1, -2, 3, -4]):    # takes abs and walks it down the list...
    print(elt)                          # ... iterating through each part of it.
                                        # prints 1, 2, 3, 4 on each line


print()
print("*** Gneral HOP = general map ***")

L1 = [1, 28, 36]
L2 = [2, 57, 9]

for elt in map(min, L1, L2):    # determines the function diffrence between the...
    print(elt)                  # ... lists and produces that function applied
                                # for instance, in the example provided the...
                                # ... output would be the min of both lists...
                                # .. in this case it prints 1, 28, 9
                                
    