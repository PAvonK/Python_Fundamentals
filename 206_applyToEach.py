# functions as objects - 5000

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
def timesFive(a):
    return a * 5

def plus1(a):
    return a + 1

def square(a):
    return a ** 2

testList = [1, -4, 8, -9]

applyToEach(testList, timesFive)
print(testList)

testList = [1, -4, 8, -9]

applyToEach(testList, abs)
print(testList)

testList = [1, -4, 8, -9]

applyToEach(testList, plus1)
print(testList)

testList = [1, -4, 8, -9]

applyToEach(testList, abs)
print(testList)
applyToEach(testList, square)
print(testList)

