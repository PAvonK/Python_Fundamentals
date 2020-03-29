# mutation / aliasing - 5000


print("*** Example 1 ***")
print("*** Example of Aliasing ***")
a = 1
b = a
print(a)    # - both a and b print to 1... any changed made to a will also ...
print(b)    # - ... be represented in b since b is an alias of a

warm = ['red', 'yellow', 'orange']
hot = warm  # since hot equals warm, hot is an alias for warm and points to...
            # ... warm also, any changed mare to warm are also made to hot

hot.append('pink')
print(hot)  # both hot and warm print the new list afte the appended action ...
print(warm) # ... they both print ['red', 'yellow', 'orange', 'pink']

print()
print("*** Example 2 ***")
print("*** Printing is the not the same as aliasing ***")

cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']

print(cool) # unlike example 1, in this case both cool and chill are...
print(chill)# ... to the same string rather than one assigned to the other...
            # ... so here if you print both they will return the same result...
            # ... but they are not the same.

chill[2] = 'blue' # Because cool and chill are not the same, with this change...
print(chill)      # ...being made it will only make the change to chill...
print(cool)       # ...but it will not make the change to cool.

print()
print("*** Example 3 ***")
print("*** Cloning a List ***")
twocool = ['blue', 'green', 'grey']
twochill = twocool[:]   # cloning make a s copy / clone of a list which is...
                        # ... which is not the same as Aliasing...
                        # ... since it is a copy . clone any changes make...
                        # ... to the original will not be made to clone and...
                        #vise versa
twocool.append('silver')
twochill.append('black')
print(twochill)         # prints ['blue', 'green', 'grey', 'black']
print(twocool)          # prints ['blue', 'green', 'grey', 'silver']

print()
print("*** Example 4 ***")
print("*** Sorting lists ***")

warm = ['red', 'yellow', 'orange']
sortedwarm = warm.sort()
print(warm)     # The variable warm has now been changed to the sorted value...
                # ...rather than printing ['red', 'yellow', 'orange'], it...
                # ... now prints ['orange', 'red', 'yellow']
print(sortedwarm)#Notive that this returns None, because it is not assigned... 
                # ... to a new variable since it is already assigned to the...
                # ... original variable

newcool = ['grey', 'green', 'blue']
sortedcool = sorted(newcool) # In this scenario a new variable is created...
                                # ... that holds the sorted list
print(newcool)      # Still prints the original list
print(sortedcool)   # Prints the sorted list

print()
print("*** Example 5 ***")
print("*** Nested Lists and issues ***")
warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]


brightcolors.append(hot) # Notices that we are appending the hot list to...
                            # ... the brightcolors list
print(brightcolors)

hot.append('pink')      # Because of appending hot to brighcolors, now that...
                        # we have appended 'ping' to hot. this means that...
                        # ... because of aliasing the hot append is also...
                        # ... affecting the brightcolors list
print(hot)
print(brightcolors)

print(hot + warm)
print(hot)

