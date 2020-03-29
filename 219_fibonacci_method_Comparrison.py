# fibonacci without dictionary - 6000 (for comparrison)


def fib_inefficient(n):     # Using if / elif / else
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_inefficient(n-1) + fib_inefficient(n-2)


def fib_efficient(n, d):    # Recursive with dictionary method
    if n in d:              # Storing Base Case
        return d[n]         # simply returning n if base case is there.
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d) # Here is the ...
        d[n] = ans              #... recursive method, d[n] = ans stores...
        return ans              #... the dicionary item.
        
d = {1:1, 2:2}

argToUse = 40
print("")
print('using fib_inefficient')
print(fib_inefficient(argToUse))
print("")
print('using fib_efficient')
print(fib_efficient(argToUse, d))
