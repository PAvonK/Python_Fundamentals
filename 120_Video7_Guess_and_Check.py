# Guess and Check - 2000, 

print("")
print("*** Guess and Check example 1 - while loop / only positive int ***")
print("")
x = int(input('Enter and integer: '))
ans = 0
while ans**3 < x:
    ans = ans + 1
if ans**3 != x:
    print(str(x) +'  is not a perfect cube.')
else:
    print("Cube root of " + str(x) + " is " + str(ans))
    
print("")
print("*** Guess and Check example 2 p while loop / pos + negative int***")
print("")
x = int(input('Enter an Interger: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + ' is not a perfect cube')
else:
    if x < 0:
        ans = - ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))
    
print("")
print("*** Guess and Check example 3 - for loop / pos + negative int***")
print("")
cube = int(input('Enter an Interger: '))
for guess in range(cube+1):
    if guess**3 >= cube:
        break
if guess**2 != abs(cube):
    print(cube, 'is not a perfect cube')
else:
    if cube < 0:
        guess = - guess
    print("Cube root of ", cube, " is ", guess)