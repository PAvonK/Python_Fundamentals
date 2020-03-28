# Searching and Sorting = 11000 (Bubble sort)

# bubble sort algorithm

'''
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(l, len(L)):
            if l[j-l] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-l]
                l[j-l] = temp
'''

# inner for loop is for doing the comparisons

# outer while loop is for doing multiple passes until no more swaps

# O(n^2) where n is len(L)
#    to do len(L)-1 comparisons and len(L)-1 passes


def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        print(L)
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp


test = [1, 5, 3, 8, 4, 2, 9, 6]

'''
Result of test...

bubble_sort(test)
[1, 5, 3, 8, 4, 2, 9, 6]
[1, 3, 5, 4, 2, 8, 6, 9]
[1, 3, 4, 2, 5, 6, 8, 9]
[1, 3, 2, 4, 5, 6, 8, 9]
[1, 2, 3, 4, 5, 6, 8, 9]
'''