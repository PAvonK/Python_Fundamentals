# Object Oriented Prorgramming - 9000 (static methods)

# learnig difference between static methods and regular methods and class methods.

# instance methods automatically pass self as the first argument
# class methods automatically pass cls as the first argument 
# static methods do not automatically pass any argument, they behave somewhat
#   similar to how functions behave

class Employee:

    raise_amt = 1.04  
    emp_num = 0           
    emp_id = 1001        

    def __init__(self, first, last, pay):
        self.first = first        
        self.last = last          
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.emp_id = Employee.emp_id 
        Employee.emp_id += 1          
                                        
        Employee.emp_num += 1

    def fullname(self):     
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  
        self.pay = int(self.pay * Employee.raise_amt)
        
    @classmethod  
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod            
    def from_string(cls, emp_str): 
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
       # A give away to see if something sould be a static method as opposed...
       #    to a regular method is if the method calls the instance or...
       #    class in anyway. if it does not, it most likely needs to be a ...
       #    static method.

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

import datetime
my_date_sun = datetime.date(2016, 7, 10)
my_date_mon = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date_sun)) # prints False
print(Employee.is_workday(my_date_mon)) # prints True




