# A for-loop will iterate through a list and provide each iteration in the statement block
# The range(x) function creates an interator from 0 to x-1 and stores it our target variable
for i in range(5):
    print('i is', i)

# Strings are interable objects.  A for-loop will loop through each letter
for letter in "The quick brown fox jumped over the lazy dog":
    print(letter)

# We can combine loops with conditions to search for a value
for number in range(10):
    if number % 3 == 0:
        print("{} divided by 3 equals 0".format(number))

# We can stop searching if we only care about the first match by breaking from the loop
for number in range(10):
    if number % 3 == 0:
        print("The first match: {} divided by 3 equals 0".format(number))
        break

# We can skip to the next iteration by using the continue-statement
for number in range(10):
    if number % 3 == 0:
        continue
    print("{} divided by 3 does not equal 0".format(number))

# A while-loop tests a condition each time before it executes
x = 0
while x < 5:
    print('x is', x)
    x = x + 1

# while-loops can also use break and continue
test_number = 0
while True:
    test_number = test_number + 1

    if test_number > 10:
        break

    if test_number % 3 == 0:
        continue

    print('test_number is %d' % test_number)

# Loops can be nested within each other
for i in range(5):
    for j in range(5):
        print('i == {}, j == {}'.format(i, j))

# TODO: Print out the multiplication table up to 9
