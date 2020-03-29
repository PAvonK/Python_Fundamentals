# Object Oriented Prorgramming - 9000 (Hierarchies)


# Video_6_Hierarchies

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname):
        self.name = newname
    
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    
class Cat(Animal):
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)

class Rabbit(Animal):
    def speak(self):
        print("meep")
    def __str__(self):
        return "rabbit:"+str(self.name)+":"+str(self.age)
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) #Creating the instance from the actual Animal class
        Animal.__init__(self, name)
        self.friends = []
    def get_friends(self):
        return self.friends
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.get_age() - other.get_age() #Dont, know why this line is causing issues, it works find in the video
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", -diff, "years younger than", other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

import random
    
class Student(Person):  # Now student is drawing on person which is drawing on Animal
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self= major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need sleep")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am wathcing tv")
    
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    


#jelly = Cat(1)
#jelly.get_name()
#jelly.set_name("JellyBelly")
#jelly.get_name()
#
#peter = Rabbit(5)
#
##print(jelly.speak())
##print(peter.speak())
#
#phil = Person('phil', 47)
#steve = Person('steve', 49)
#
#tiesha = Person('tiesha', 43, 'Course VI')






    












