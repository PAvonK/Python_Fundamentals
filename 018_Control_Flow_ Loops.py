# Input / Output - 2000, Iteration - 2000 (for loops)

print("*** While Loops ***")

n = input("You are in the Lost Forest. go left or right? ")
while n == "right":
    n = input("You are in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest")

n = 0
while n < 5:
    print(n)
    n = n+1
    

print("*** For loops ***")


for n in range(5):
    print(n)
    