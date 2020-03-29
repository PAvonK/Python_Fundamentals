# Input / Output - 2000, Strings - 2000 (concatenation)

print("*** Output ***")
print("")
x = 1
print(x) #Prints value 1 which by itslef cannot be added to a string
x_str = str(x) #This will cast or conver the value of x which is 1 into
#    a string and give it a name which is x_str
print("my fav num is:", x, ".", "x =", x)  #All different expressions
#   Seperated by a comma to make one cohesive string in printout
print("my fav num is " + x_str + ". " + "x = " + x_str) #All different 
#   expressions seperated by a comma to make one cohesive string in printout

print("*** Input ***")
text = input("Type anything... ")
print(5*text)

num = int(input("Type and number... "))
print(5*num)