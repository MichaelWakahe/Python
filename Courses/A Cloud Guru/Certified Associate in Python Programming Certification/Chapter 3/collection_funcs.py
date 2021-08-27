"""
Higher order functions take other functions as arguments, or can return functions.
"""

domain = [1, 2, 3, 4, 5]

# Map examples

# f(x) = 1 + x
our_range = map(lambda x: 1 + x, domain)
print(f"First range is {list(our_range)}")


def squared(x: int) -> int:
    return x * x


our_range = map(squared, domain)
print(f"Second range is {list(our_range)}")

# Filter examples
even_numbers = filter(lambda x: x % 2 == 0, domain)
print(f"Even numbers are {list(even_numbers)}")

# Reduce
from functools import reduce

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(f"The reduced numbers are {the_sum}")

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print(f"Sorting by default: {sorted(words)}")

print("Sorting with key:")
print(sorted(words, key=lambda s: s.lower()))


words.sort(key=str.lower, reverse=True)
print(f"Sorting with method: {words}")
