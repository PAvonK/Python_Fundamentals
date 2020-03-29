# Object Oriented Prorgramming - 9000 (Hierarchies / Methods)

# Q - Thinking about the genPrimes generator from the last problem, which of the
# following can be done only by using a generator, instead of defining a
# function (that uses any type of construct we've learned about, except
# generators)?

# Return 1000000 prime numbers
# Print every 10th prime number, until you've printed 20 of them
# Keep printing the prime number until the user stops the program
# Everything that can be done with generator can be done with a function - Correct!!



# Q - Every procedure that has a yield statement is a generator.

# True - Correct!!
# False


# Q - If a procedure has only one yield statement, but that statement will
#   never be executed, then the procedure is not a generator.

# True
# False - Correct!!


# Q - If we were to use a generator to iterate over a million numbers, how
#   many numbers do we need to store in memory at once?

# 1
# 2 - Correct!!
# 1000
# 1000000
# Don't need to store anything in memory


# For the following tasks, would it be best to use a generator, a standard
#   function, or either?

# Q - Finding the nth Fibonacci number

# Generator
# Standard function - Correct!!
# Either a generator or standard function is fine


# Q - Printing out an unbounded sequence of Fibonacci numbers

# Generator - Correct!!
# Standard function
# Either a generator or standard function is fine


# Q - Printing out a bounded sequence of prime numbers, where the prime
#   numbers are successively computed by division by smaller primes

# Generator
# Standard function
# Either a generator or standard function is fine - Correct!!


# Q - Printing out an unbounded sequence of prime numbers, where the prime
#   numbers are successively computed by division by smaller primes

# Generator - Correct!!
# Standard function
# Either a generator or standard function is fine


# Q - Finding the score of a word from the 6.00x Word Game of Pset 4

# Generator
# Standard function - Correct!!
# Either a generator or standard function is fine


# Q - Iterating over a sequence of numbers in a random order, where no number
#   is repeated

# Generator
# Standard function - Correct!!
# Either a generator or standard function is fine
