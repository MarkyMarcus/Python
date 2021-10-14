import states

print 'The first 13 states are:'
# TODO: Print the first 13 states in the state.union list
i = 0
while i < 13:
    print states.union[i]
    i = i + 1

print ''

print 'All of the states are:'
# TODO: Print all of the states in the states.union list
for state in states.union:
    print state

print ''

# TODO: Print the state name for a two-letter abbreviation
print 'The state with abbreviation of MD is: ', states.states['MD']
