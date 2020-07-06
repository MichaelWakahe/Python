"""
Python Object Types: Dictionaries

Examples are tested in Python 3
"""
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print("D['food'] is {}".format(D['food']))  # Fetch value of key 'food'
D['quantity'] = D['quantity'] + 1   # Add 1 to 'quantity' value, alternatively: D['quantity'] += 1
print("D is {}".format(D))


D = {}
D['name'] = 'Bob'   # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
print("D is {}".format(D))

bob1 = dict(name='Bob', job='dev', age=40)  # Keywords
print("\nbob1 is {}".format(bob1))
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))    # Zipping
print("bob2 is {}".format(bob2))


rec = {'name': {'first': 'Bob', 'last': 'Smith'},
        'jobs': ['dev', 'mgr'],
        'age': 40.5}
print("\nrec['name']['last'] is {}".format(rec['name']['last']))    # Index the nested dictionary
rec['jobs'].append('janitor')   # Expand Bob's job description in place
print("rec is {}".format(rec))

D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99 # Assigning new keys grows dictionaries
print("\nD is {}".format(D))
print("'f' in D? {}".format('f' in D))
value = D.get('x', 0)   # Index but with a default
print("value is {}".format(value))

print("\nSorting Keys: for Loops")
Ks = list(D.keys()) # Unordered keys list
Ks.sort()   # Sorted keys list
for key in Ks:  # Iterate though sorted keys
    print(key, '=>', D[key])    # <== press Enter twice here (3.X print)

for key in sorted(D):   # Alternative way of sorting
    print(key, '=>', D[key])


squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print("\nsquares is {}".format(squares))

# A long way of achieving the above
squares2 = []
for x in [1, 2, 3, 4, 5]:   # This is what a list comprehension does
    squares2.append(x ** 2)  # Both run the iteration protocol internally
print("squares2 is {}".format(squares2))
