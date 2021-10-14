import re

story = '''
A Day at the Zoo!

Today I went to the zoo. I saw a {ADJECTIVE} {NOUN} jumping up
and down in its tree. He {VERB: PAST TENSE} {ADVERB} through the large tunnel
that led to its {ADJECTIVE} {NOUN}. I got some peanuts and passed them through
the cage to a gigantic gray {NOUN} towering above my head. Feeding that animal
made me hungry. I went to get a {ADJECTIVE} scoop of ice cream. It filled my
stomach. Afterwards I had to {VERB} {ADVERB} to catch our bus. When I got home
I {VERB: PAST TENSE} my mom for a {ADJECTIVE} day at the zoo.
'''

# Get missing terms
keywords = re.findall(r"{([^}]+)}", story)

for keyword in keywords:
    term = input("Please enter a %s: " % keyword)
    story = story.replace('{%s}' % keyword, term, 1)

print(story)
