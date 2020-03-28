# Searching and Sorting = 11000, Branching = 1000, Iteration = 2000

# Here is some code for linear search that uses the fact that 
#     a set of elements is sorted in increasing order:

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

# Consider the following code, which is an alternative version 
#     of search.

def search1(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

# Which of the following statements is correct? You may assume 
#     that each function is tested with a list L whose elements 
#     are sorted in increasing order; for simplicity, assume L 
#     is a list of positive integers.


# search and search1 return the same answers.
# search and search1 return the same answers provided L is non-empty.
# search and search1 return the same answers provided L is 
#     non-empty and e is in L.
# search and search1 do not return the same answers.
# search and search1 return the same answers for lists of 
#     length 0 and 1 only.

# correct = search and search1 return the same answers.

# Explanation:

# It is equally valid to iterate over the indicies of a list 
#     (as in search) or iterate over the elements of the list 
#     itself (as in search1). As we've seen, Python's for 
#     statement iterates over the items of any sequence 
#     (a list or a string), in the order that they appear in the 
#     sequence. As an example, assume L = [4, 9, 2]. The statement

# for i in range(len(L)):
#     is actually the statement

# for i in range(3): 
#     which is actually the statement

# for i in [0, 1, 2]: 
#     So iterating over the indicies of a list (as in search) is 
#         almost identical to iterating over the elements of the list 
#         itself - the statement

# for i in L: 
#     is actually the statement

# for i in [4, 9, 2]: 
#     Both methods of iteration are equally valid. At the end of the 
#         day, you should iterate in a way that makes sense to you.