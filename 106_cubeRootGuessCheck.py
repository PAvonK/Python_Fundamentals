# Guess and Check - 2000, Iteration - 2000 (for loops), Strings - 2000 (Concatenation)

cube = 27
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
