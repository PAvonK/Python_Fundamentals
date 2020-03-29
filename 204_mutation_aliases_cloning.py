# lists - 5000, types - 1000

aList = [0, 1, 2, 3, 4, 5]
bList = aList
aList[2] = 'hello'
aList == bList # = boolean tupe, True should be trusted

aList is bList   # Answer True
type(aList is bList) # Type boolean

aList # [0, 1, 'hello', 3, 4, 5]
type(aList) # type list

bList # answer same as aList [0, 1, 'hello', 3, 4, 5] because bList is an aList
type(bList) # type list

cList = [6, 5, 4, 3, 2]
dList = []
for num in cList:       # This iterates over cList making a clone / copy of...
    dList.append(num)   # ... it.
cList == dList          # This is true because both contained lists are the...
                        # ... even though the variables themseves are not one...
                        # ... in the same

cList is dList # False becasue they are clones and not aliases
type(cList is dList) # boolean


cList[2] = 20
cList   # prints [6, 5, 20, 3, 2] becasue the 2nd index element was changed to 20

dList   # prints [6, 5, 4, 3, 2] because since dList is merely a clone of cList, ...
        # ... the changed made to cList will not be passed to dList
        
        

            
                     
                        

