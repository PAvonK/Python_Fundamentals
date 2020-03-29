# lists - 5000 / dictonaries - 6000 comparrison

animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

animals # returns {'a': 'aardvark', 'b': 'baboon', 'c': 'coati', 'd': 'donkey'}
        # to console

animals['c'] #return 'coati' to console

animals['donkey'] # returns an error ('donkey' is value not keys)

len(animals) # returns 4 (4 keys /  value pairs in dict)

animals['a'] = 'anteater' #changes 'aardvark' to 'anteater'
animals['a'] # returns 'anteater to console'

len(animals['a']) # returns 8 (There are 8 letters in 'anteater')

'baboon' in animals #False (baboon is a value... 'b' is in animals)

'donkey' in animals.values() #True because 'donkey' exists and is a values

'b' in animals # returns True (The key 'b' is there)

animals.keys() # returns ['a', 'b', 'c', 'd'] or dict_keys(['a', 'b', 'c', 'd'])

del animals['b'] # deletes 'b' keys
len(animals) #returns 3( we deleted the 4th ('b' = 'baboon'))

animals.values() # prints dict_values(['anteater', 'coati', 'donkey']) (This is
                    #the current value list)

                    
