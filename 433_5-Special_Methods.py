# Object Oriented Prorgramming - 9000 (Special methods)

class Employee:

    raise_amount = 1.04 
    emp_num = 0        
    emp_id = 1001       

    def __init__(self, first, last, pay):   # all of these will be able ...
        self.first = first                  # to be used on multiple sub...
        self.last = last                    # classes like developers and managers
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.emp_id = Employee.emp_id 
        Employee.emp_id += 1          
                                        
        Employee.emp_num += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    def __repr__(self): #used by developers for debugging
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
    
    def __str__(self): #meant to be used and read by te developer
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

    
emp_1 = Employee('Corer', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(len('test'))      # Same
print('test'.__len__()) # Same

print(len(emp_1))

print(emp_1 + emp_2)  # Because of the Dunder add method defined above




#print(emp_1)

#print(emp_1.__repr__())
#print(emp_1.__str__())

# Special methods for Arithmatic




