# Computational Complexity = 10000, O(n) / O(1), Branching = 1000, Iteration = 2000

# Program 1

def program1(L):                    # L = empty list
    multiples = []                  # 1
    for x in L:                     # -- No list
        for y in L:                 # --
            multiples.append(x*y)   # --
    return multiples                # 1 
                                    # total 2
## Best Case = 2
## Worse Case = 3*n**2 + n + 2 steps

# What is the number of steps it will take to run Program 1 in 
#    the best case? Express your answer in terms of n, the 
#    number of elements in the list L. You can assume list 
#    appending takes 1 step.

#  Correct 2 = O(n^2)

# What is the number of steps it will take to run Program 1 in 
#    the worst case? Express your answer in terms of n, the 
#    number of elements in the list L. You can assume list 
#    appending takes 1 step.


#  Correct 3*n^2 + n + 2 = O(n^2)

# Explanation:

# In the best case scenario, L is an empty list. So we execute 
#    only the first assignment statement, then the return 
#    statement. Thus in the best case we execute 2 steps. 
#    Note that since the list is empty, no assignments are 
#    performed in the for x in L line.

# In the worst case scenario, L is a long list. In this case we 
#    go through the loop for x in L n times. Every time through 
#    this loop, we execute an assignment of a value to x, and 
#    then the inner loop for y in L. The assignment takes 1 step 
#    on each iteration; how many steps does the inner loop take 
#    on each iteration?

# The inner loop has three operations (assignment of a value 
#    to y, x*y, and list appending). So the inner loop executes 
#    3*n times on each iteration of the outer loop. Thus the 
#    nested loop structure is executed 
#    n * (3*n + 1) = 3*n**2 + n times!

# Adding in two steps (for the first assignment statement, 
#    and the return statement) we see that in the worst case, 
#    this program executes 3*n**2 + n + 2 steps. 

# Program 2:

# Best Case
def program2(L):
    squares = []
    for x in L:
        for y in L:
            if x == y:
                squares.append(x*y)
    return squares
## Best Case = 2
## Worse Case = 4*n**2 + n + 2 steps

# What is the number of steps it will take to run Program 2 
#    in the best case? Express your answer in terms of n, 
#    the number of elements in the list L.


#  Correct 2 O(1)
 
# What is the number of steps it will take to run Program 2 in 
#    the worst case? Express your answer in terms of n, the 
#    number of elements in the list L.


#  Correct 4*n^2 + n + 2 = O(n^2)

# Explanation:

# In the best case scenario, L is an empty list. So we execute 
#    only the first assignment statement, then the return 
#    statement. Thus in the best case we execute 2 steps. 
#    Note that since the list is empty, no assignments are 
#    performed in the for x in L line.

# In the worst case scenario, L is a long list of one repeated 
#    number (ie [2, 2, 2, 2, ...]. In this case we go through 
#    the loop for x in L n times. Every time through this loop, 
#    we perform one assigment of a value to the variable x, then 
#    we execute the inner loop for y in L n times.

# The inner loop performs one assigment of a value to the 
#    variable y. It then has one operation that is checked 
#    every time (if x == y). Since the WORST case is when the 
#    list is composed of identical elements, this check is 
#    always true - so the third and fourth operations (x*y, 
#    and list appending) are always performed. So the inner 
#    loop executes 4*n times on each iteration of the outer 
#    loop. Thus the nested loop structure is executed 
#    n * (4*n + 1) = 4*n**2 + n times!

# Adding in two steps (for the first assignment statement, 
#    and the return statement) we see that in the worst case, 
#    this program executes 4*n**2 + n + 2 steps.

# Program 3:

def program3(L1, L2):
    intersection = []
    for elt in L1:
        if elt in L2:
            intersection.append(elt)
    return intersection
## Best Case = 2
## Worse Case = n**2 + 2*n + 2 steps

# What is the number of steps it will take to run Program 3 
#    in the best case? Express your answer in terms of n, the 
#    number of elements in the 
#    list L1 (assume len(L1) == len(L2)).


#  Correct 2 = O(1)

# What is the number of steps it will take to run Program 3 
#    in the worst case? Express your answer in terms of n, the 
#    number of elements in the list L1 (assume len(L1) == len(L2)).


#  Correct n^2 + 2*n + 2 = O(n^2)

# Explanation:

# In the best case scenario, L1 is an empty list. So we execute 
#    only the first assignment statement, then the return 
#    statement. Thus in the best case we execute 2 steps.

# In the worst case scenario, every element of L1 is the same 
#    as the very last element of L2. In this case we go through 
#    the loop for elt in L1 n times. Every time through this 
#    loop, we perform one assigment of a value to the variable 
#    elt, then we execute the check if elt in L2.

# How long does it take to execute this check? Well in the 
#    worst case, elt is the very LAST element of L2. In order 
#    to check if elt in L2, Python iterates over the elements 
#    of L2 until it either finds the one you're looking for, 
#    or L2 runs out of elements. Thus in the worst case, the 
#    check if elt in L2 takes n steps. After this, we perform 
#    one append operation. So the conditional plus the append 
#    takes n + 1 steps on each iteration of the loop. Thus the 
#    for loop takes n * (n + 2) = n**2 + 2*n steps!

# Adding in two steps (for the first assignment statement, 
#    and the return statement) we see that in the worst case, 
#    this program executes n**2 + 2*n + 2 steps.

# In the last video, Professor Grimson introduced the idea of 
#    "asymptotic complexity", which means we describe running 
#    time in terms of number of basic steps. We've described 
#    the best- and worst-case running times in terms number of
#     basic steps for the three programs above. Now, we'd like 
#     you to give the complexity order (ie, "Big O" running time) 
#     of each of the above programs.

# Recall that "Big O" notation gives an upper bound on 
#    asymptotic growth of a function. So, should you use the 
#    best-case or the worst-case running times for each 
#    program? Review the video again if you're unsure of what 
#    to put for the following boxes.

# Note: Your answer should be expressed with a capital 
#    letter O, then a mathematical term similar to one described 
#    in the introduction to this problem - for example, O(n^5).

# What is the complexity order of Program 1?

#    Correct O(n^2)

# What is the complexity order of Program 2?

#    Correct O(n^2)
  
# What is the complexity order of Program 3?

#    Correct O(n^2)

# Explanation:

# Remember the following rules when determining the complexity 
#    order of a function:

# If running time is a sum of multiple terms, keep one with the 
#    largest growth rate (so n**3 + 100n**2 + 500,000 is O(n**3)).

# If the remaining term is a product (eg 3n**2), drop any 
#    multiplicative constants (so 3n**2 is O(n**2)).

# It's also good to note that if you have a function that 
#    takes a constant number of steps - regardless of the size 
#    of the input - the function is O(1), even if it takes 
#    3,000,000 steps every time! This is because the function 
#    does not take any additional time as the input grows large.

# Finally, pay attention to the fact that 
#    Programs 1, 2, and 3 were all O(n**2). This is important!
#     Generally, a nested loop structure has O(n**2) complexity. 
#     This is not the best, as we'll discover in the next 
#     lectures in this sequence.
