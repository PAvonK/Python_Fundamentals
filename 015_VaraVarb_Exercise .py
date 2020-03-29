# Branching - 1000 (if / elif / else)

varA = 0
varB = 9

if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print('smaller')  

    '''
    Explanation

Is type(varA) == str or type(varB) == str equivalent to type(varA) or type(varB) == str ? Those are not equivalent because of Python precedence (some operations have higher precedence than others). The == has higher precedence than the or so it will get evaluated first. Therefore:
type(varA) or type(varB) == str
Will evaluate to the following, if we explicitly put parentheses:
type(varA) or ( type(varB) == str )
True or ( type(varB) == str )
( True )
Because "anything" or "True" will just take the value of "True" (by boolean algebra).
And the other expression:
type(varA) == str or type(varB) == str
Will evaluate to the following, if we explicitly put parentheses:
( type(varA) == str ) or ( type(varB) == str )
So you will have to check each of the expressions in the parentheses to see whether they are true or not to determine the final result. So these two are not equal.

Hint: Remember the type function?

Hint: Recall that if you want to check whether the type of a variable is a specific kind, you can compare the type of the variable to the type of a known object.
'''