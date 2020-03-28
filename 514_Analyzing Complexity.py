# Computational Complexity = 10000, O(n^2)

# Quadratic Complexity

def isSubset(L1, L2):   # Does every element of the first 
                        #   list also occur in the second list
    for e1 in L1:
        matched = False         # sets match to false
        for e2 in L2:           
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True

# characteristics of quadratic Loop within a loop which is a part
#   polynomial...