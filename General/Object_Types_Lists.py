"""
Python Object Types: Lists

Examples are tested in Python 3
"""

L = [123, 'spam', 1.23]

print ("len(L) is {}".format(len(L)))
print ("L[0] is {}".format(L[0]))   # Indexing by position
print ("L[:-1] is {}".format(L[:-1]))   # Slicing a list returns a new list
print ("L + [4, 5, 6] is {}".format(L + [4, 5, 6]))   # Concat/repeat make new lists too
print ("L * 2 is {}".format(L * 2))
print ("L is {}".format(L)) # We're not changing the original list

L.append('NI')
print ("After L.append('NI'), L is {}".format(L))  # Growing: add object at end of list

L.pop(2)
print ("After L.pop(2), L is {}".format(L)) # Shrinking: delete an item in the middle
                                            # "del L[2]" deletes from a list too

# Because lists are mutable, most list methods also change the list
# object in place, instead of creating a new one:
print ("\n")
M = ['bb', 'aa', 'cc']
M.sort()
print ("M is {}".format(M))

M.reverse()
print ("M is {}".format(M))

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print ("M is {}".format(M))
print ("M[1] is {}".format(M[1]))   # Get row 2
print ("M[1][2] is {}".format(M[1][2]))     # Get row 2, then get item 3 within the row

print ("\nlist comprehension expression")
col2 = [row[1] for row in M]   # Collect the items in column 2
print ("col2 is {}".format(col2))
# for more serious number crunching you will probably want to use one of the numeric extensions to Python,
# such as the open source NumPy and SciPy systems.

list1 = ['eggs', 'spam', 'ham']
print ("'ham' in list1? {}".format('ham' in list1)) # Test membership

print ("\ndemonstrating range")
print ("list(range(4)) is {}".format(list(range(4))))   # 0..3 (list() required in 3.X)
print ("list(range(-6, 7, 2)) is {}".format(list(range(-6, 7, 2))))  # -6 to +6 by 2 (need list() in 3.X)
print ("list(map(sum, M)) is {}".format( list(map(sum, M) ))) # Map sum over items in M
print ("{sum(row) for row in M} is {}".format({sum(row) for row in M}))    # Create a set of row sums (a set)
print ("{i : sum(M[i]) for i in range(3)} is {}".format( {i : sum(M[i]) for i in range(3)} ))  # Creates key/value table of row sums (a dictionary)

