# lists - 5000, list operations - 5000, iteration - 2000


bList = []
aList = [1, 2, 3]
count = 3
while count > 0:
    temp = aList.remove(0)
    bList.append(temp)
    print(bList)
    count -= 1
