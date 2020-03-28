# Lists = 5000, Iteration = 2000

# In this problem, we'll examine how indirection works. Consider 
#     the following definitions:

a = [1, 2, 3, 4, 0]
b = [3, 0, 2, 4, 1]
c = [3, 2, 4, 1, 5]

# What is the value of the following expressions? If you think 
#     there will be an error, please type in 'error' (without 
#     quotes) in the input box.

# a[0] = correct 1

# b[1] = correct 0

# a[a[1]] = correct 3

# b[b[2]] = correct 2

# a[b[2]] = correct 3

# c[a[b[3]]] = correct 3

# a[c[a[b[0]]]] = correct error

# a[c[a[b[3]]]] = correct 4

# Assume we have defined the following function:

def foo(L):
    val = L[0]
    while (True):
        val = L[val]

# Which of the following statement(s) will result in an 
#     infinite loop?

# foo(a)
# foo(b)
# foo(c)
# correct
# Explanation:

# The function foo first binds val to the 0th element of L, L[0]. 
#     Then, val is bound to element L[L[0]], then L[L[L[0]]], 
#     and so on.

# Calling foo on lists a and b results in an infinite 
#     loop - foo(a) traverses indicies 0->1->2->3->4->0 and 
#     foo(b) traverses indicies 0->3->4->1->0.

# foo(c) results in an error, because L[5] does not exist.

# Consider the following code:

num = 1
L = [5, 0, 2, 4, 6, 3, 1]
val = 0
for i in range(0, num):
    val = L[L[val]]

print(val)

# What is the smallest value that num can be such that the 
#     number 3 is printed?

# 0 = correct

# Now, we redefine L to be:

# L = [2, 0, 1, 5, 3, 4]
# What is the smallest value that num can be such that the 
#     number 3 is printed?

# Impossible = correct

# Explanation:

# When L = [5, 0, 2, 4, 6, 3, 1], we need to set num = 1 to 
#     get 3 to print out.

# When L = [2, 0, 1, 5, 3, 4], there is no way to get to the 
#     number 3 if we start from val = 0, because the indirection 
#     structure for L is (0->2->1->0, 3->5->4->3).