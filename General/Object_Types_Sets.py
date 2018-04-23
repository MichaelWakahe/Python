"""
Python Object Types: Sets

Examples are tested in Python 3
"""
X = set('spam') # Make a set out of a sequence in 2.X and 3.X
Y = {'h', 'a', 'm'} # Make a set with set literals in 3.X and 2.7

print ("X, Y is {}".format(X, Y))   # A tuple of two sets without parentheses
print ("X & Y is {}".format(X & Y)) # Intersection
print ("X | Y is {}".format(X | Y)) # Union
print ("X - Y is {}".format(X - Y)) # Difference
print ("X > Y? {}".format(X > Y)) # Superset

list1 = list(set([1, 2, 1, 3, 1]))  # Filtering out duplicates (possibly reordered)
print ("list1 is {}".format(list1))

set1 = set('spam') - set('ham') # Finding differences in collections
print ("set1 is {}".format(set1))

print ("Are these 2 sets equal? {}".format(set('spam') == set('asmp'))) # Order-neutral equality tests

print ("'p' in set1? {}".format('p' in set1))   # membership





