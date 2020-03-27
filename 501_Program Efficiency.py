# Computational Complexity = 10000, O(n) / O(1) / O(log n), Branching = 1000, Iteration = 2000

# Best Case                 Step Sequence
def program1(x):            # x = 0        
    total = 0               # 1 = 1
    for i in range(1000):   # 2 = 1 x 1000    
        total += i          # 3 = 2 x 1000 (total = total + i)

    while x > 0:            # 4 = 1
        x -= 1              # --  (x is not greater than 0)
        total += x          # --  (x is not greater than 0)

    return total            # 5 = 1

                           #1 + 3*1000 + 1 + 1 = 3003 steps

# What is the number of steps it will take to run Program 1 in the best 
#    case? Express your answer in terms of n, the size of the input x.

#    Correct 3003 = O(1)

# Worst Case
def program1(x):            # x = Large Int
    total = 0               # 1 = 1
    for i in range(1000):   # 2 = 1 x 1000
        total += i          # 3 = 2 x 1000 (total = total + i)
        
                            # Following loop is ran n times
    while x > 0:                # 4 = n x 1
        x -= 1              # 5 = n x 1 + n x 1 (x = x - 1)
        total += x          # 6 = n x 1 + n x 1 (total = total + x)

    return total            # 7 = 1
                            # 1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003 steps

# What is the number of steps it will take to run Program 1 in the 
#   worst case? Express your answer in terms of n, the size of the input x.

#    Correct 5*n + 3003 = O(n)

# Explanation:

# In the best case scenario, x is less than or equal to 0. We first 
#    execute the assignment total = 0 for one step. Next we execute the 
#    for i in range(1000) loop. This loop is executed 1000 times and has 
#    three steps (one for the assignment of i each time through the loop, 
#    as well as two for the += operation) on each iteration. We next 
#    check if x > 0 - it is not so we do not enter the loop. Adding one 
#    more step for the return statement, in the best case we execute 
#    1 + 3*1000 + 1 + 1 = 3003 steps.

# In the worst case scenario, x is a large positive number. In this 
#    case, we first execute the assignment total = 0 for one step. Next 
#    we execute the first loop 1000 times (3000 total steps), then we 
#    execute the second loop (while x > 0) n times. This loop has five 
#    steps (one for the conditional check, x > 0, and two each for 
#    the -= and += operations). When we finally get to the point 
#    where x = 0, we execute the conditional check x > 0 one last time - 
#    since it is not, we do not enter the loop. Adding one more step for 
#    the return statement, in the worst case we 
#    execute 1 + 3*1000 + 5*n + 1 + 1 = 5*n + 3003 steps.

# Best Case
def program2(x):            # x = 0
    total = 0               # 1 = 1
    for i in range(1000):   # 2 = 1 * 1000
        total = i           # 3 = 1 * 1000

    while x > 0:            # 4 = 1
        x = x//2            # -- (x is not greater that 0)
        total += x          # -- (x is not greater that 0)

    return total            # 5 = 1
                            # 1 + 2*1000 + 1 + 1 = 2003 steps  

# What is the number of steps it will take to run Program 2 in the best 
#    case? Express your answer in terms of n, the size of the input x.

#    Correct 2003 O(1)

# What is the number of steps it will take to run Program 2 in the 
#    worst case? Express your answer in terms of n, the size of the input x.

# Worst Case
def program2(x):            # x = large int
    total = 0               # 1 = 1
    for i in range(1000):   # 2 = 1 x 1000
        total = i           # 3 = 1 x 1000

                            # Divide by 2 each time to log2(n)
    while x > 0:            # 5 = 1 x log2(n)
        x = x//2            # 6 = 1 x log2(n) + 1 x log2(n)
        total += x          # 7 = 1 x log2(n) + 1 x log2(n)

    return total            # 8 = 1
            # 1 + 2*1000 + 5*(log2(n) + 1) + 1 + 1 = 5*log2(n) + 2008 steps

#    Correct 5*log2(n) + 2008 = O(log n)

# Explanation:

# In the best case scenario, x is less than or equal to 0. We first 
#    execute the assignment total = 0 for one step. Next we execute the 
#    for i in range(1000) loop. This loop is executed 1000 times and has 
#    two steps (one for the assignment of i each time through the loop, 
#    as well as one for the = operation) on each iteration. We next check 
#    if x > 0 - it is not so we do not enter the loop. Adding in one step 
#    for the return statement, in the best case we execute 
#    1 + 2*1000 + 1 + 1 = 2003 steps.

# In the worst case scenario, x is a large positive number. In this case 
#    we first execute the assignment total = 0 for one step, then we execute 
#    the first loop 1000 times (2000 total steps). Finally execute the 
#    second loop (while x > 0) log2(n) + 1 times. This is tricky! Because 
#    we divide x by 2 every time through the loop, we only execute this 
#    loop a logarithmic number of times. log2(n) divisions of x by 2 will 
#    get us to x = 1; we'll need one more division to get x <= 0 . Don't 
#    worry if you couldn't get this fact; we'll go through it a few more 
#    times in this unit.

# This while loop has five steps (one for the conditional check, x > 0, 
#    and two each for the //= and += operations). When we finally get to 
#    the point where x = 0, we execute the conditional check x > 0 one 
#    last time - since it is not, we do not enter the loop. Adding in one 
#    step for the return statement, in the worst case we execute 
#    1 + 2*1000 + 5*(log2(n) + 1) + 1 + 1 = 5*log2(n) + 2008 steps.

# Best Case
def program3(L):                    # L = empty list
    totalSum = 0                    # 1 = 1
    highestFound = None             # 2 = 1
    for x in L:                     # -- (no list to operate on)
        totalSum += x               # -- (no list to operate on)

    for x in L:                     # -- (no list to operate on)
        if highestFound == None:    # -- (no list to operate on)
            highestFound = x        # -- (no list to operate on)
        elif x > highestFound:      # -- (no list to operate on)
            highestFound = x        # -- (no list to operate on)

    return (totalSum, highestFound) # 3 = 1
                                    # 1 + 1 + 1 = 3

# What is the number of steps it will take to run Program 3 in the 
#    best case? Express your answer in terms of n, the number of elements 
#    in the list L.

#    Correct 3 = O(1)

# Worst Case
def program3(L):                    # L = large list
    totalSum = 0                    # 1 = 1
    highestFound = None             # 2 = 1
    for x in L:                     # 3 = n x 1
        totalSum += x               # 4 = n x 1 + n x 1

    for x in L:                     # 5 = n x 1
        if highestFound == None:    # 6 = n x 1
            highestFound = x        # 7 = n x 1
        elif x > highestFound:      # 8 = n x 1
            highestFound = x
                                    # 2 + 3*n + 4*n - 1 + 1= 7*n + 2 steps

    return (totalSum, highestFound)

# What is the number of steps it will take to run Program 3 in the 
#    worst case? Express your answer in terms of n, the number of elements 
#    in the list L.

#    Correct 7*n + 2 = O(n)

# Explanation:

# In the best case scenario, L is an empty list. Thus we execute only 
#    the first two assignment statements, then the return statement. Therefore 
#    in the best case we execute 3 steps. Note that since the list is empty, 
#    no assignments are performed in the for x in L lines.

# In the worst case scenario, L is a list with its elements sorted in 
#    increasing order (eg, [1, 3, 5, 7, ...]). In this case we execute the 
#    first two assignment statements (2 steps). Next we execute the first 
#    loop n times. This first loop has three steps (one for the assignment 
#    of x each time through the loop, as well as two for the += operation), 
#    adding 3*n steps.

# Finally we execute the second loop n times. The first time we execute 
#    this loop, we perform 3 steps - one for the assignment of x; then we 
#    run the check if highestFound == None, and finding it to be True, we 
#    execute the assignment highestFound = x.

# The next (n-1) times we execute this loop, we perform 4 steps: one for 
#    the assignment of x, then we run the check if highestFound == None, and 
#    finding it to be False, we run the check elif x > highestFound. Since 
#    this is always True (the list is sorted in increasing order), we 
#    execute the assignment highestFound = x. Therefore in the second loop 
#    we execute 3 + (n-1)*4 = 3 + 4*n - 4 = 4*n - 1 steps.

# Finally we execute the return statement, which is one more step.

# Pulling this all together, we can see that in the worst case we 
#    execute 2 + 3*n + 4*n - 1 + 1= 7*n + 2 steps.