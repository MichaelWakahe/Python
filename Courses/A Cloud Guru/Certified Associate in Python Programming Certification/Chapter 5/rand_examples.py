"""
Examples with the `random` module.
"""
import random

# If you seed in the same way, the same random sequence of numbers is generated.
print("Demonstration of using the same seed")
random.seed(10)
print(random.random())
print(random.random())

random.seed(10)
print(random.random())
print(random.random())

sentence = "Python also has the standard while-loop, and the *break* and *continue* statements work as in C++ and " \
           "Java, altering the course of the innermost loop"
my_list = sentence.split()

# Random choice
print(f"\nRandom choice is: {random.choice(my_list)}")

# Random sample
print(f"\nRandom sample of 3 is: {random.sample(my_list, 3)}")

# Shuffling
random.shuffle(my_list) # This only works on mutable objects
print(f"\nShuffled list is: {my_list}")
