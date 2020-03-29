# tuples - 5000, operations (slicing) - 5000

"""
Created on Thu Feb 13 13:41:51 2020

@author: pavk1

Write a procedure called oddTuples, which takes a tuple as input, and returns 
a new tuple as output, where every other element of the input tuple is 
copied, starting with the first one. So if test is the tuple 
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input 
would return the tuple ('I', 'a', 'tuple').
"""


aTup = ('I', 'am', 'a', 'test', 'tuple')
       
def oddTuple(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return aTup[0::2]
print(oddTuple(aTup))

    
