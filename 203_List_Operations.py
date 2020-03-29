# list operations - 5000

"""
Operations are all done in order
"""

listA = [1, 4, 3, 0]
listB = ['x', 'z', 't', 'q']

listA.sort # = function
type(listA.sort) # = function

listA.sort() # = None - The sort is done but without a print command it will
                #not put out a response
type(listA.sort()) # = Nonetype

listA # = [0, 1, 3, 4]
type(listA) # = list

listA.insert(0, 100) # = None
type(listA.insert(0, 100)) # - Nonetype

listA.remove(3) # = None
type(listA.remove(3)) # = removed the item but since  there is no print funcion
                        # nothing will be returned
                        
listA.append(7) # = None
type(listA.append(7)) # = same as other nonetypes above

listA # = [100, 0, 1, 4, 7]
type(listA) # - list

listA + listB # = [100, 0, 1, 4, 7, 'x', 'z', 't', 'q']
type(listA + listB) # = list

listB.sort() # = sorts list B
listB.pop() # = pops the 'Z' off the end of the list

listB.count('a') # = 0
type(listB.count) # = int

listB.remove('a') # = error
type(listB.remove('a')) # = Nonetype

listA.extend([4, 1, 6, 3, 4]) # =- error
type(listA.extend([4, 1, 6, 3, 4])) # = Nonetype

listA.count(4) # = 3
type(listA.count(4)) # = int

listA.index(1) # = 2
type(listA.index(1)) # = int

listA.pop(4) # = 7
type(listA.pop(7)) # = pops 7 off the list

listA.reverse() # = None
type(listA.reverse()) # = Nonetype

listA # = [4, 3, 6, 1, 4, 4, 1, 0, 100]
type(listA) # = list
