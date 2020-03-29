# Iteration - 2000, Branching - 1000, lists - 5000,
#   list operations - 5000

import webbrowser

def flatten(aList):
    newList = []
    for item in aList:
        if type(item) != type([]):
            newList.append(item)
        else:
            newList.extend(flatten(item))
    return newList

print(flatten([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))

#uncomment line below and run program to open link to python tutor of this problem
webbrowser.open("http://pythontutor.com/live.html#code=def%20flatten%28aList%29%3A%0A%20%20%20%20newList%20%3D%20%5B%5D%0A%20%20%20%20for%20item%20in%20aList%3A%0A%20%20%20%20%20%20%20%20if%20type%28item%29%20!%3D%20type%28%5B%5D%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20newList.append%28item%29%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20newList.extend%28flatten%28item%29%29%0A%20%20%20%20return%20newList%0A%0Aprint%28flatten%28%5B%5B1,'a',%5B'cat'%5D,2%5D,%5B%5B%5B3%5D%5D,'dog'%5D,4,5%5D%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-live.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false")
     
print(flatten(([1, 2, 3, 4], [5, [6, 7], 8], [8, 10, [11], 12])))     