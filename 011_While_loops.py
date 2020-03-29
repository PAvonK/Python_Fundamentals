# Iteraton - 2000 (for loops, while loops), Strings - 2000,
#   

print("Primary Example")
iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 
    

print("\n Test 1")
'''
Test 1 does not work because it runs into an infite loop do to the fact
that there is no way to termiate it.  ''for the sake of this test I added
a break statement to prevent it''

Another issue is that it does not have a way to incriment the "incriment"
'''
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break #I added this break only so it did not get into initite loop on test

print("\n Test 2")
''' 
for Test 2 the reason it does not return the same result it because of the 
location of the break, it essentially breaks the loop count =+ 1 after the first 
cycle so it runs the 5 times but does not advance.

Another issue is that it does not have a way to incriment the "incriment"
'''
for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        break 

print("\n Test 3")
'''
Test 3 produces the same as sample because within the for loop the iteration is
advanced by both count and index.

It is being terminated by the ffor index inside wich is before the while
'''
count = 0
phrase = "hello, world"
for iteration in range(5):
    index = 0
    while index < len(phrase):
        count += 1
        index += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))

print("\n Test 4")
'''
Count in advnacing by the number that is in the len of the phrase which is 12

termiation is happening becasue of the while true function:
'''
count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
print("\n Test 5")
'''
very similar to 4 except that it has been shrunk down by removing uncessary
parts of the code.
'''
count = 0
phrase = "hello, world"
for iteration in range(5):
    count += len(phrase)
    print("Iteration " + str(iteration) + "; count is: " + str(count))