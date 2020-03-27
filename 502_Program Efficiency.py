# Computational Complexity = 10000, O(n) / O(1), Branching = 1000, Iteration = 2000

def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False
"""
Choose which of the following inputs to linearSearch would give the best 
    case, average case, or worst case run time.

Choose which of the following inputs to linearSearch would give the best 
case, average case, or worst case run time.

Best Case Run Time


linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)
correct
Worst Case Run Time


linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)
correct
Average Case Run Time


linearSearch([14, 15, 6, 27, 13, 16, 25, 11, 7], 15)
linearSearch([21, 1, 25, 22, 30, 13, 7, 24, 12], 24)
linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 20)
linearSearch([9, 3, 12, 24, 7, 8, 23, 11, 19], 8)
linearSearch([4, 12, 20, 17, 9, 14, 7, 24, 6], 7)
linearSearch([13, 9, 22, 3, 10, 17, 11, 2, 12], 26)
correct

What is the number of steps it will take to run linearSearch in the best 
    case? Express your answer in terms of n, the number of elements in the 
    list L.

Indicate addition and multiplication explicitly, with + and * symbols. 
    Indicate exponentiation with the caret (^) symbol.

  Correct = 1 = O(1)

Explanation:

In the best case scenario, L is an empty list. Thus one step is taken: 
    return False.

What is the number of steps it will take to run linearSearch in the worst 
    case? Express your answer in terms of n, the number of elements in the 
    list L.

Indicate addition and multiplication explicitly, with + and * symbols. 
    Indicate exponentiation with the caret (^) symbol.

  Correct = 2*n + 1 = O(n)

Explanation:

In the worst case scenario, x is not present in L. Thus we go through 
    the for loop n times. This means we execute assignment of e to each 
    element of L (this takes place in the line for e in L) to enter the for 
    loop, and also execute the check...

        if e == x:
    ...once each for every element. So this is 2*n steps. Finally at the end 
    of the for loop, we execute the return statement one time.

"""
