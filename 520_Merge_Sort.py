# Searching and Sorting 11000, 
#   Computational / Searching Complexity = 10000, 
#   Iteration = 1000, Branching = 2000, #   Lists = 5000

# # After_Video_6_Merge_Sort_Exercise_7
 
# Exercise 7
 
# This problem will walk through some applications of complexity 
#     analysis. Suppose you're asked to implement an application. 
#     One of the things it has to do is to report whether or not 
#     an item, x, is in a list L. L's contents do not change over 
#     time. Below are two possible ways to implement this 
#     functionality. Assume that mergeSort is implemented as per 
#     the lecture.
 
# L is a list with n items.
 
# Application A:
 
# Every time it's asked to, it performs a linear search through 
#     list L to find whether it contains x.
 
 
# Application B:
 
# Sort list L once before doing anything else (using mergeSort). 
#     Whenever it's asked to find x in L, it performs a binary 
#     search on L.
 
 
# If the application is asked to find x in L exactly one time, 
#     what is the worst case time complexity for Application A?
 
# O(1)
# O(logn)
# O(n)        = Correct
# O(nlogn)
# O(n2)
# correct = O(n)
 
# Explanation:
 
# Application A just performs one linear search through n elements. 
#     This is O(n) complexity.
 
# If the application is asked to find x in L exactly one time, 
#     what is the worst case time complexity for Application B?
 
 
# O(1)
# O(logn)
# O(n)
# O(nlogn)     = Correct
# O(n2)
 
# correct = O(nlogn) 
 
# Explanation:
 
# The time complexity for Application B is how long it takes to 
#     do mergeSort once, plus how long it takes to do a binary 
#         search. That works out to O(nlogn+logn), which is 
#             just O(nlogn).
 
# If the application is asked to find x in L k times, what is the 
#     worst case time complexity for Application A?
# 
# 
# O(1)
# O(k+logn)
# O(k+n)
# O(kn)       = Correct
# O(n+klogn)
# correct = O(kn)
 
# Explanation:
 
# We have to do k linear searches so the time complexity is O(kn).
 
# If the application is asked to find x in L k times, what is 
#     the worst case time complexity for Application B?
 
 
# O(kn)
# O(nlogn)
# O(n+klogn)
# O(nlogn+klogn)  = Correct
# O(knlogn+logn)
# correct = O(nlogn+klogn)
# Explanation:
 
# Doing the search k times means that the time complexity is 
#     how long it takes to do mergeSort once, plus how long it 
#     takes to do a binary search k times. That works out to 
#     O(nlogn+klogn). Since we don't know what the value of k 
#     is, we cannot simplify further.
 
# What value(s) of k would make Application A be faster (i.e., 
#     asymptotically grow slower than) Application B?
 
# 
# k=1         = Correct
# k=n
# k=logn
# k=n2
# k=2n
# correct = k=1
 
# Explanation:
 
# When k=1, Application A's complexity is O(kn)=O(n), and 
#     Application B's complexity is O(nlogn+klogn)=O(nlogn+logn).
 
# Setting k at any value greater than 1 makes O(kn) asymptotically 
#     grow faster than O(nlogn+klogn).
 
# What value(s) of k would make Application A grow at the same 
#     rate as Application B?
 
 
# k=1
# k=n
# k=logn      = Correct
# k=n2
# k=2n
# correct = k=logn
 
# Explanation:
 
# When k=logn, Application A's complexity is O(kn)=O(nlogn), and 
#     Application B's complexity is O(nlogn+klogn)=O(nlogn+lognlogn). 
#     lognlogn grows slower than nlogn, so in this case Application
#     B's time complexity is O(nlogn). So, when k=logn, the order 
#     of time complexity of Applications A and B are equal.
 
# Which application should you choose if you know that there are 
#     going to be n3 requests to find x in L?
 
 
# Application A
# Application B
# correct
# Explanation:
 
# When k=n3, Application A has time complexity O(n4) whilst 
#     Application B's time complexity is O(n3logn). Generally 
#     we can extrapolate that for very large k, Application B will 
#     be the preferred choice.

# SubmitSome problems have options such as save, reset, hints, or 
#     show answer. These options follow the Submit button.