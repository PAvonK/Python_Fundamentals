# Approximate Solutions - 3000

x = 25
epsilon = 0.01
step = epsilon**2
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    ans += step
    numGuesses += 1
 #   print(ans)
print("numGuesses = ", numGuesses)
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, "is close to square root of", x)
    

# The below code is not right at the moment. need to revisit to see how to
    # make the square root work even in negative numbers
x = -123456
epsilon = -0.01
numGuesses = 0
low = x
high = 0
ans = (high + low)/2.0
while (ans**2 + x) <= epsilon:
    print("low =", low, "high = ", high, "ans = ", ans)
    numGuesses += 1
    if ans**2 > x:
        high = ans
    else:
        low = ans
    ans = (high + low)/2    
print("numGuesses = ", numGuesses)
print(ans, "is close to square root of ", x)
        