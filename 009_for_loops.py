# Iteration - 2000, Operators - 1000 (Modulo %), 
#   Strings - 2000 (Concatenation), Branching - 1000


print("")
print("*** Exercise 6 problem 1 ***")
print("")
myStr = '6.00x'

for char in myStr:
    print(char)

print('done')

print("")
print("*** Exercise 6 problem 2 ***")
print("")
greeting = 'Hello!'
count = 0

for letter in greeting:
    count += 1
    if count % 2 == 0:
        print(letter)
    print(letter)

print('done')

print("")
print("*** Exercise 6 problem 3 ***")
print("")
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
