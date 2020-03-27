# Computational Complexity = 10000, O(n) / O(1) / O(n^2) / O(log(n))

# After_Video_4and5_Analyzing_Complexity_Exercise_6

# Consider the following Python procedures. For each one, specify 
#   its order of growth.

# Assume n has been previously bound to some value

# i = 0
# while i < 5:
#    n *= 2
#    i += 1

# print(n)
 
#  correct = O(1)

# def iterPower(a, b):
#    result = 1
#    while b > 0:
#       result *= a
#       b -= 1
#    return result
 
#  correct = O(b)

# def recurPower(a, b):
#    print(a, b)
#    if b == 0:
#       return 1
#    else:
#       return a * recurPower(a, b-1)
 
#  correct = O(b)

# def recurPowerNew(a, b):
#    print(a, b)
#    if b == 0:
#       return 1
#    elif b%2 == 0:
#       return recurPowerNew(a*a, b/2)
#    else:
#       return a * recurPowerNew(a, b-1)
 
#  correct = O(log(b))