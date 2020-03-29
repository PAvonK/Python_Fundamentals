# tuples - 5000

x = (1, 2, (3, "John", 4), "Hi")

x[0] # = 1
type(x[0]) # = int

x[2] # = (3, "John", 4)
type(x[2]) # = tuple

x[-1] # = "Hi"
type(x[-1]) # = string

x[2][2] # = 4
type(x[2][2]) # = int

x[2][-1] # = 4
type(x[2][-1]) # = string

x[-1][-1] # = i
type(x[-1][-1]) # = string

x[-1][-2] # = error because value does not exist...
type(x[-1][2]) # = Nonetype / error

x[0:1] # = (1,)
type(x[0:1]) # = tuple

x[0:-1] # (1, 2, (3, "John", 4),)
type(x[0:-1]) # = tuple

len(x) # = 4
type(len(x)) # = int

2 in x # = True
type(2 in x) # = boolean

3 in x # = False
type(3 in x) # = boolean

x[0] = 8 # = error becasue tuples cannot be modified...
type(x[0] = 8) # = Nonetype / error
