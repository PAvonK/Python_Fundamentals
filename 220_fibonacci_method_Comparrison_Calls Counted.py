# fibonacci with dictionary - 6000 (for comparrison)

def fib_inefficient(n):
    global numFibCalls  #Global call which allows for calling outside of scope...
    numFibCalls += 1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib_inefficient(n-1) + fib_inefficient(n-2)


def fib_efficient(n, d):
    global numFibCalls  #Global call which allows for calling outside of scope...
    numFibCalls += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans



numFibCalls = 0
fibArg = 34

print(fib_inefficient(fibArg))
print('function calls', numFibCalls)

numFibCalls = 0

d = {1:1, 2:2}
print(fib_efficient(fibArg, d))
print('function calls', numFibCalls)
