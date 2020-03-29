# Iteration - 2000 (while loops)

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

'''
Following code returns infinite loop
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
'''

'''
Following code returns infinite loop
num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num))
'''
print("")
print("*** While Exercise 1 ***")
print("")
num = 0
while num < 10:
    num = num + 2
    print(num)
print("Goodbye!")

print("")
print("*** While Exercise 2 ***")
print("")
print("Hello!")
n = 10
while n > 0:
    print(n)
    n -= 2
    
print("")
print("*** While Exercise 3 ***")
print("")
end = 6
new_total = 0
mysum = 0
while mysum <= end:
    new_total += mysum 
    mysum += 1
print(new_total)


print("")
print("*** for Exercise 1 ***")
print("")
num = 0
for i in range(2, 12, 2):
    print(i)
print("Goodbye!")   

print("")
print("*** for Exercise 2 ***")
print("")
print("Hello!")
n = 10
for n in range(10, 0, -2):
    print(n)
    

print("")
print("*** for Exercise 3 ***")
print("")
end = 6
mysum = 0
for i in range(end+1):
    mysum += i
print(mysum)

   

    
    
