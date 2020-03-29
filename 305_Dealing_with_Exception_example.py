# Exceptions and Assertions - 8000


try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a/b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")

'''
Tell me one number:2

Tell me another number:0
Bug in user input.
Outside
'''