# Object Oriented Prorgramming - 9000 (property decorators)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        

    @property  # Getter...
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @property  # Getter
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @fullname.setter # Setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter # Setter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

emp_1.fullname = 'Corey Schafer'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.first)

