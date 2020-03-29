# 5000 - lists, types 1000

"""
Operations are all done in order
"""
x = [1, 2, [3, "John", 4], "Hi"]

x[0] # = 1
type(x[0]) # = int

x[2] # = [3, "John", 4]
type(x[2]) # = list

x[-1] # = "Hi"
type(x[-1]) # = string

x[2][2] # = 4
type(x[2][2]) # = int

x[0:1] # = [1]
type(x[0:1]) # = list

2 in x # = True
type(2 in x) # = boolean

3 in x # = False
type(3 in x) # = boolean

x[0] = 8 # = [8, 2, [3, "John", 4], "Hi"]
type(x[0] = 8) # = list. This is not an error because lists can be modified
