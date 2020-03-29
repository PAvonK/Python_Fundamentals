# Exceptions and Assertions - 8000 (exception)

while True:
    try:
        n = input("please enter an int:")
        n = int(n)
        break
    except ValueError:
        print("Input not an integet; try again")
print("Correct input of an integer!")