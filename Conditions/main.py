# An if-statement can used to control which statements are executed.
# The expression is evaluated as True or False.  True results are executed
if True:
    print('The result was True')

if False:
    print('This statement will not execute')

# Simple if-statements can be put on one line
if 1 > 0: print('Python says 1 is greater than 0')

# An statement block can have one or more statements but they *must* be indented the same way
if True:
    print('This statement will execute')
    print('So will this one')
    print('.. and this one too')

# An if-statement can have an else-clause but only 1
if False:
    print('This will not execute')
else:
    print('But this statement will execute')

# An if-statement can have any number of elif-statements.  elif is short for else-if
if False:
    print('This will not execute')
elif True:
    print('This will execute')
elif True:
    print('This will NOT execute because the previous condition was True')

# The else clause will only execute if all other conditions were False
if False:
    print('This will not execute')
elif False:
    print('Neither will with one')
elif False:
    print('Nope.  Not this one either')
else:
    print('But this statement will execute')

# TODO: Calculate your age and store it in a variable.  Create a if/elif/else statement that
# uses the age in an expression and in the printed messages
age = 2019 - 2001
if age < 13:
    print('At age %d, you are not a teenage yet' % age)
elif age < 20:
    print('At age %d, you are a teenage' % age)
else:
    print('At age %d, you are older than a teenage' % age)
