# Approximate Solutions - 3000

"""
The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give 
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!

Here is a transcript of an example session:
    
Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Note: your program should use input to obtain the user's input! Be sure to 
handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the 
user explaining you did not understand their input. Then, you should re-ask 
the question, and prompt again for input. For example:
    
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c

"""

print("Please guess a number between 0 and 100: ")
guess_count = 0
l = 0
h = 100
ans = (h + l)//2 #Floor division key here.

while guess_count < 50:
    print("is your secret number: ", ans)
    guess = str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    guess_count += 1
    if guess == "l":
        l = ans
    elif guess == "h":
        h = ans
    elif guess != "l" and guess != "h" and guess != "c":
        print("Sorry, I did not understand your input.")
    else:
        break
    ans = (l + h)//2 #Floor division key here.
  
print("Game over. Your secret number was: ", ans)    