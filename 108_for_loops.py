# Iteration - 2000 (for loops, Branching - 1000, 
#   Operators - 1000 (Modulo %))


print("")
print("*** Exercise 5 #1 ***")
print("")
num = 10
for num in range(5):
    print(num)
print(num)

print("")
print("*** Exercise 5 #2 ***")
print("")
divisor = 2
for num in range(0, 10, 2):
    print(num/divisor)

print("")
print("*** Exercise 5 #3 ***")
print("")
for variable in range(20):
    if variable % 4 == 0:
        print(variable)
    if variable % 16 == 0:
        print('Foo!') 

print("")
print("*** Exercise 5 #4 ***")
print("")
for letter in 'hola':
    print(letter) 

print("")
print("*** Exercise 5 #5 ***")
print("")
count = 0
for letter in 'Snow!':
    print('Letter # ' + str(count) + ' is ' + str(letter))
    count += 1
    break
print(count)

