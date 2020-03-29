# dictionaries - 6000, iteration - 2000

list = []
dict1 = {'a':1, 'b':2, 'c':0}

for key in dict1.keys():
    list.append(key)
str1 = ' '.join(list)
print(str1)  

print()
print()

tempDict = {}
for k, v in dict1.items():
    if v > 0:
        tempDict.update({k:v})

print(tempDict)
        