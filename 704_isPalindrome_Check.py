# Branching - 1000, Strings - 2000, 

# Write a Python function that returns True if aString is a palindrome 
#    (reads the same forwards or reversed) and False otherwise. Do not 
#    use Python's built-in reverse function or aString[::-1] to 
#    reverse strings.

# This function takes in a string and returns a boolean.

def isPalindrome(aString):
    '''
    aString: a string
    '''
    # Your code here
    testString = ''

    for char in aString:
        testString = char + testString
    if aString == testString:
        return True
    else:
        return False

print(isPalindrome('steve'))
