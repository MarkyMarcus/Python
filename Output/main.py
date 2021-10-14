# print() can be used to print numbers, strings, expressions, objects
print(1)
print('Hello')
print(1 + 1)
print(print)

# print() can be used to combine values into one message
print('I am', 10, 'years old')

# format specifiers make combining values easier
# format specifiers:
#   %d - Number
#   %s - String
#   %f - Number with decimal
print('I am %d years old' % 10)
print('My name is %s' % 'Michelle')
print('I am %f inches tall' % 40.25)

# Multiple format specifiers must be in parenthesis
print('My name is %s and I am %s years old' % ('Michelle', 10))

# Another way is to use the string's format() function
print('I am {} years old'.format(10))
print('My name is {}'.format('Michelle'))
print('My name is {} and I am {} years old'.format('Michelle', 10))
print('My name is {0} and I am {1} years old'.format('Michelle', 10))
print('My name is {1} and I am {0} years old'.format(10,'Michelle'))

# TODO: Print out your name and age using format specifiers
print('My name is %s and I am %d years old' % ('Michelle', 15))

# TODO: Print out your name and age using the format function
print('My name is {} and I am {} years old'.format('Michelle', 15))
