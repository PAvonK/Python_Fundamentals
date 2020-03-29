# Object Oriented Prorgramming - 9000 (Instance Variables)

class Employee:

    raise_amount = 1.04  # Class Variables
    emp_num = 0           # Class Variables
    emp_id = 1001        # Class Variables

    def __init__(self, first, last, pay):
        self.first = first        # Instance Variables
        self.last = last          # Instance Variables
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.emp_id = Employee.emp_id # adds emp ID from class variables to...
        Employee.emp_id += 1          # ... each employee then moves the...
                                      # ... emp_id up for the next employee  
        Employee.emp_num += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)



print(Employee.emp_num)     # prints 0 employees
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(Employee.emp_num)     # prints 2 employees 



print(emp_1.emp_id)
print(emp_2.emp_id)

print(emp_1.pay)        # previous pay for emp_1
emp_1.apply_raise()     # applying the riase amount to emp_1
print(emp_1.pay)        # New pay


