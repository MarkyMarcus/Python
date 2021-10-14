# Create a simple dictionary
my_dict = {"a": 1, "b": 2}
print(my_dict)

# Individual items in a list can be referenced by key
eng2esp = {'Sunday': 'domingo', 'Monday': 'lunes', 'Tuesday': 'martes', 'Wednesday': 'miercoles', 'Thursday': 'jueves', 'Friday': 'viernes', 'Saturday': 'sabado'}
print(eng2esp['Sunday'])
print(eng2esp)

# We can iterate through the list to get keys and values
for key, value in eng2esp.items():
    print("key:", key, "value:", value)

# Values can be added several ways
my_dict = {}                        # []
my_dict['a'] = 1                    # {'a': 1}
my_dict.update({"b": 2})            # {'a': 1, 'b': 2}, Update is done "in place"

# Values can be removed by name
my_dict.pop('a')            # {'b': 2}, returns '1'

# TODO: Create a dictionary of your eye color, hair color, favorite color and print out the list
