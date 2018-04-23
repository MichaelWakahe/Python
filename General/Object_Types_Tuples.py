"""
Python Object Types: Tuples

Examples are tested in Python 3
"""
T = (1, 2, 3, 4)    # A 4-item tuple
print ("len(T) is {}".format(len(T)))    # Length

print ("T + (5, 6) is {}".format(T + (5, 6)))   # Concatenation
print ("T[0] is {}".format(T[0]))   # Indexing, slicing, and more

print ("T.index(4) is {}".format(T.index(4)))   # Tuple methods: 4 appears at offset 3
print ("T.count(4) is {}".format(T.count(4)))   # 4 appears once

#T[0] = 2 # Tuples are immutable, this will generate an error

T = (2,) + T[1:]    # Make a new tuple for a new value
print ("T is {}".format(T))

# the parentheses enclosing a tuple’s items can usually be omitted, as done here:
T = 'spam', 3.0, [11, 22, 33]
print ("T[1] is {}".format(T[1]))
print ("T[2][1] is {}".format(T[2][1]))

