# Create a simple string
string = 'the quick brown fox jumped over the lazy dog.'

# We can get the length of a string
print(len(string))

# Make the entire string uppercase
print(string.upper())

# Make the entire string lowercase
print(string.lower())

# Just capitalize the first word
print(string.capitalize())

# Capitalize every word
print(string.title())

# Append to a string
print(string + '  That string has every letter.')

# We can break the string apart into individual words with split().  Uses the space to separate the string.
print(string.split())

# We can search if a string contains another string
print(string.find('fox'))

# Comparing two strings can be done with the '==' operator
print('First string' == 'First string')

# TODO: Create a string and replace all lowercase vowels characters with an uppercase vowels.  Hint: use string.replace()
string = 'This is my string'
print(string.replace('a', 'A').replace('e', 'E').replace('i', 'I').replace('o', 'O').replace('u', 'U'))
