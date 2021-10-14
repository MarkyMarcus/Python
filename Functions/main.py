# The most basic function takes zero parameters and doesn't return a value
# Functions are called by using the name with parenthesis
def basic():
    print('I am a very simple function')

basic()

# Functions that are never called won't be executed
def very_important():
    print('I will not be printed because I am never called')


# Functions can take parameters.  They become variables only seen within the function and
# don't effect variables elsewhere
def print_sum(a, b):
    print('The sum of {} and {} is {}'.format(a, b, a + b))

print_sum(1, 3)

# Functions can return a value
def get_sum(a, b):
    return a + b

total = get_sum(1, 3)
print('The total is', total)

# Parameters can have default values by setting an initial value.  These parameters are optional.
def multiply(a, b=1):
    return a * b

print("The product of 3 and 3 is", multiply(3, 3))
print("The product of 3 and the default is", multiply(3))

# Functions calling themself is called recursion.
def factorial(a):
    if a == 1:
        return a
    return a * factorial(a - 1)

print("The factorial of 10 is", factorial(10))

# TODO: Create a function that prints the multiplication table for a value and call the function
