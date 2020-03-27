# Lists - 5000, Iteration - 2000, Branching - 1000

# Write a function called longestRun, which takes as a parameter a 
#     list of integers named L (assume L is not empty). This function 
#     returns the length of the longest run of monotonically increasing 
#     numbers occurring in L. A run of monotonically increasing numbers 
#     means that a number at position k+1 in the sequence is either 
#     greater than or equal to the number at position k in the sequence.
 
# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your 
#     function should return the value 5 because the longest run of 
#     monotonically increasing integers in L is [3, 4, 5, 7, 7].

def longestRun(L):
    """
    Input: List of positive integers ex. [10, 4, 3, 8, 4, 5, 7, 7, 2]
    output: length of longest monotonically increasing numbers list
    ex. [3, 4, 5, 7, 7]
    """
    # Your code here

    count = 1
    runningCount = 1

    for i in range(len(L) -1):
        if L[i+1] >= L[i]:
            count += 1
            if count > runningCount:
                runningCount = count
        else:
            count = 1
    
    return runningCount

# Tests
print(longestRun([0]))
print(longestRun([1,1,1,1,1]))
print(longestRun([10, 4, 6, 8, 3, 3, 4, 5, 7, 7, 2, 9]))
print(longestRun([7, 4, 1, -7, -11]))
print(longestRun([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longestRun([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))
print(longestRun([10, 4, 3, 8, 3, 4, 5, 7, 7, 2]))

            

