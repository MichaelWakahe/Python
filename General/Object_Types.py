"""
Introducing Python Object Types

Examples are tested in Python 3
"""
import math
import random


#####################
# Numbers
#####################
print ("'2 ** 10' is: ", (2 ** 10))
#print ("How many digits in a really BIG number? ", len(str(2 ** 1000000)))
print ("math.pi is ", math.pi)
print ("math.sqrt(85) is ", math.sqrt(85))
print ("random.random() is ", random.random())
print ("random.choice([1, 2, 3, 4]) is ", random.choice([1, 2, 3, 4]))


#####################
# Strings
#####################
print ("\n")
S = 'Spam'

#------------------------------------------------
print ("Strings: Sequence Operations")
print ("S is", S)
print ("len(S) is", len(S))
print ("S[1] is", S[1])
print ("S[-1] is", S[-1])  # The last item in S
print ("S[-2] is", S[-2])
print ("S[1:3] is", S[1:3])    # Slice of S from offsets 1 through 2 (not 3)
print ("S[1:] is", S[1:])  # Everything past the first (1:len(S))
print ("S[:3] is", S[:3])  # Same as S[0:3]
print ("S[:-1] is", S[:-1])    # Everything but the last again, but simpler (0:-1)
print ("S[:] is", S[:])  # All of S as a top-level copy (0:len(S))
print ("S is", S)  # S itself hasn't changed

print ("S + 'xyz' is", S + 'xyz')   # Concatenation
print ("S * 8 is", S * 8)   # Repetition
print ("S is", S)  # S itself hasn't changed


#------------------------------------------------
print ("\nStrings: Immutability")
#S[0] = 'z'  # Error: Immutable objects cannot be changed
S = 'z' + S[1:] # But we can run expressions to make new objects
print ("S is", S)

S = 'shrubbery'
L = list(S) # Expand to a list: [...]
print ("L is", L)   # ['s', 'h', 'r', 'u', 'b', 'b', 'e', 'r', 'y']
L[1] = 'c'  # Change it in place
print ("''.join(L) is", ''.join(L))  # Join with empty delimiter - 'scrubbery'

B = bytearray(b'spam')  # A bytes/list hybrid (ahead)
B.extend(b'eggs')   # 'b' needed in 3.X, not 2.Xs
print ("B is", B)   # B[i] = ord(c) works here too
bytearray(b'spameggs')
print ("B.decode() is", B.decode())  # Translate to normal string - 'spameggs'


#------------------------------------------------
print ("\nStrings: Type-Specific Methods")
S = 'Spam'
print ("S.find('pa') is", S.find('pa')) # Find the offset of a substring in S
print ("S.replace('pa', 'XYZ') is", S.replace('pa', 'XYZ')) # Replace occurrences of a string in S with another
print ("S is", S)  # S itself hasn't changed

line = 'aaa,bbb,ccccc,dd'
print ("line.split(',') is", line.split(','))   # Split on a delimiter into a list of substrings
print ("S.upper() is", S.upper())   # Upper- and lowercase conversions
print ("S.isalpha() is", S.isalpha())   # Content tests: isalpha, isdigit, etc.

line = 'aaa,bbb,ccccc,dd\n'
print ("line.rstrip() is", line.rstrip())   # Remove whitespace characters on the right side
print ("line.rstrip().split(',') is", line.rstrip().split(','))      # Combine two operations

