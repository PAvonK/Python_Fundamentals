# Functions - 4000, Strings - 2000, Branching - 1000

# Book Section 4.1.1 Finger excersize

def isIn(str1, str2):
    if str1 in str2:
        print("This worked")
    elif str2 in str1:
        print("This also worked")
    else:
        print("Not so lucky this time")

isIn("Hello", "Hello again")
isIn("this is an amazing piece of information", "amazing piece")
isIn("Hello", "Goodbye")