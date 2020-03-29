# Testing and Debugging - 7000


# Bad Code

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return n
   else:
      return n * f(n-1)

# When we call f(3) we expect the result 6, but we get 0.

# When we call f(1) we expect the result 1, but we get 0.

# When we call f(0) we expect the result 1, but we get 0.

# Using this information, choose what line of code should be changed from the following choices:

# Fixed Code

def f(n):
   """
   n: integer, n >= 0.
   """
   if n == 0:
      return 1
   else:
      return n * f(n-1)
  
print(f(4))
