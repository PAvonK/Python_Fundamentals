# Object Oriented Prorgramming - 9000 (OOP and Methods)


class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None  # new born animal that does not have a name
                            # we will name it shortly
    ### Getters...    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    
    ### Setters...
    def set_age(self, newage): # This might be for a silimation where the animal is getting older
        self.age = newage
    def set_name(self, newname=""): # change name to something else
        self.name = newname
        
    def __str__(self):
        return "animal: "+str(self.name)+":"+str(self.age)
    
        
# Console or code infor here:...

myAnimal = Animal(3)
print(myAnimal) #prints animal None 3 becase a name has not yet been given
print()
myAnimal.set_name("George")
print(myAnimal) #prints name now because it has been names

myAnimal.get_age() #prints 3 in console
myAnimal.get_name() # prints 'George' in console


    












