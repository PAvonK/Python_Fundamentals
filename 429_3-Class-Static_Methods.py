# Object Oriented Prorgramming - 9000 (static methods)

# learnig difference between static methods and regular methods and class methods.

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

    def fullname(self):     # this is a regular method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):  # this is a regular method
        self.pay = int(self.pay * Employee.raise_amt)
        
    @classmethod  # this is a class method
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount
        
    @classmethod            #example of using a class method to parse stings
    def from_string(cls, emp_str): # taken from the emp_str_1 and so-on below
        first, last, pay = emp_str.split('-')
        cls(first, last, pay)
        return cls(first, last, pay)
    


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)    # because we are using a class method here,...
                                # ... setting this to 5% changes the whole...
                                # ... class raise_amt to 5% or 1.05

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)




