# Create a simple list
my_list = [2, 4, 6, 8, 10, 'hello', 5*5]
print(my_list)

# Individual items in a list can be referenced by index.  Index numbers start at 0
# 0 = Sunday
# 1 = Monday
# 2 = Tuesday
# 3 = Wednesday
# 4 = Thursday
# 5 = Friday
# 6 = Saturday
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(days_of_the_week[0])
print(days_of_the_week[6])
print(days_of_the_week)

# A list of numbers can be created quickly with the range() function passed to the list() function
numbers = list(range(100))
print(numbers)

# The length of a list can be determined with the len() function
numbers = list(range(100))
print(len(numbers))

# Values can be added several ways
my_list = []                # []
my_list = my_list + [5]     # [5]
my_list.append(7)           # [5, 7]
my_list.extend(['a', 'b'])  # [5, 7, 'a', 'b']
my_list.insert(2, 'foo')    # [5, 7, 'foo', 'a', 'b']

# Values can be removed several ways
my_list.pop()               # [5, 7, 'foo', 'a'], returns 'b'
my_list.remove('foo')       # [5, 7, 'a']

# TODO: Create a list for the months of the year.  Print 'Happy Birthday' for your birthday month.
