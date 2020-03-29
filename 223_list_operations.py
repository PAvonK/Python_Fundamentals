# Iteration - 2000, Lists - 5000, list operations - 5000


def lessThan4(aList):
    '''
    aList : a list of strings
    '''
    # Your code here
    newList = []
    for string in aList:
        if len(string) < 4:
            newList.append(string)
    return newList
                
        
print(lessThan4(["apple", "cat", "dog", "banana"]))

