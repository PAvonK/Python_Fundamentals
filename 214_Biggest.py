#d dictionaries - 6000


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):                     # Sets Function
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None                       # begins with a result of None
    maxNum = 0                          # Used to count the values

    for key in aDict.keys():            # Sets a for loop key through dict keys
        if len(aDict[key]) >= maxNum:   # Determines if value length is greater...
                                        #... than previous maxNum
            result = key                # If it is, the result changes to key
            maxNum = len(aDict[key])    # maxNum is changed to new variable
    return result                       # Returns the result

print(biggest(animals))
