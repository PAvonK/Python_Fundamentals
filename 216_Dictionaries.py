# lists - 5000 / dictonaries - 6000 comparrison

print("*** Example of Lists for comparison to Dictionaries ***")

names = ['Phil', 'Tiesha', 'Taylor']    # All different lists which holds data...
grade = ['B', 'A', 'C']                 #... by thier index number which means...
course = [2.00, 6.001, 20.002]          #... there must be the same number in ...
                                        #... each list and the data is in ...
                                        #... reality stored in different ...
                                        #... structures.
                                        
def get_grade(student, name_list, grade_list, course_list):
    i = name_list.index(student)    # takes in student, and then the various...
    grade = grade_list[i]           #... lists, has to find the index of the...
    course = course_list[i]         #... student and then pull the approriate...
    return (course, grade)          #... data based of the index.

print(get_grade('Tiesha', names, grade, course))
                                    #prints, (6.001, 'A') for course and grade
                                    
'''
--- The above solution is a messy solution
--- Must contain many lists,
--- Must always index the lists using int's. 
--- Must also remember to change multiple lists if someone new has been added.
'''

print()
print("*** Exmaple of Dictionaries for comparison to Lists ***")

my_dict = {}
grades = {'Ana':'B', 'John':'A+', 'Denise':'A'} # defines the dictionary ...
                            #... with the key as the first componenet and the...
                            #... value as the second component.

print(len(grades))
print(grades)               # prints the key and value of the dict
grades['Sylvan'] = 'A+'     # Adds a new key and value to the dict
print('John' in grades)     #tests to see if 'John is in the dict, return True if so
print('Daniel' in grades)   #returns False if not in the dict
print(grades['John'])       # prints out the variable for Key 'John'
del(grades['Ana'])          # removed Key 'Ana' from dict

print(grades.keys())    #prints an iterable of the dict keys
print(grades.values())  #Prints an iterable of the dict values

'''
--- 
'''