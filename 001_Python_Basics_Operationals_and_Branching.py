# Branching - 1000, Strings / Concatenation - 2000 

print("*** Branching Statement ***")

# If / Else Statements

x = int(input('Enter an integer for Even / Odd Test: '))
if x%2 == 0:
    print(str(x) + " is Even") # Concatenation example of string
else:
    print(str(x) + " is Odd")
print("Done with Conditionals, passing " + str(x) + " as x")


print("")
print("*** Nested Conditionals in a branching statement ***")
y = int(input("Enter an integer for divisble by 2 and 3 test: "))
if y%2 == 0:
    if y%3 == 0:
        print(str(y) + " is Divisible by 2 and 3")
    else:
        print(str(y) + " is Divisible by 2 and not by 3")
elif y%3 == 0:
    print(str(y) + " is Divisible by 3 and not by 2")
else:
    print(str(y) + " is not divisible by either 2 or 3")
print("Done with divisible test, passing " + str(y) + " as y")

print("")
z = int(input("Enter an integer to be used in comparrison to " + str(x) + " and " + str(y) + " for Boolean Test of highest value: "))
print("*** Compare Booleans ***")
if x < y and x < z:
    print(str(x) + " is least")
elif y < z:
    print(str(y) + " is least")
else:
    print(str(z) + " is least")
