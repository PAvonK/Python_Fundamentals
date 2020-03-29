# Object Oriented Prorgramming - 9000 (Hierarchies / Methods / Classes)

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    # other methods

    def __str__(self):
        """return self's name"""
        return self.name

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.name + " says: " + utterance)

class Student(MITPerson):   # This is designed just to clean up the code. 
    pass                    #   we are just making sure to pass all students...
                            #   the same way.
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, " Dude, " + utterance)
    
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student)

    
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

m1 = MITPerson('Mark Zuckerberg')
m1.setBirthday(5,14,84)
m2 = MITPerson('Drew Houston')
m2.setBirthday(3,4,83)
m3 = MITPerson('Bill Gates')
m3.setBirthday(10,28,55)
m4 = Person('Travis Kalanik')
m5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

p1 = MITPerson('Eric')
p2 = MITPerson('John Guttag')
p3 = MITPerson('John Smith')
p4 = Person('John')

MITPersonList = [m1, m2, m3, m4, m5]

s1 = UG('Matt Damon', 2017)
s2 = UG('Ben Affleck', 2017)
s3 = UG('Arash Ferdowsi', 2018)
s4 = Grad('Drew Houston')
s5 = UG('Mark Zuckerberg', 2019)
p1 = MITPerson('Eric Grimson')
p2 = MITPerson('John Guttag')
p3 = MITPerson('Ana Bell')
q1 = Person('Bill Gates')
q2 = Person('Travis Kalanick')

studentList = [s1, s2, s3, s5, s4]

allList = studentList + [p1, p2, p3] + [q1, q2]

for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)  
    
for e in MITPersonList:
    print(e)
    
print(s1.speak('where is the quiz?')) # Matt Damon says:  Dude, where is the quiz?
print(s2.speak('I have no idea!!!')) # Ben Affleck says:  Dude, I have no idea!!!
