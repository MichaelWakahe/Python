"""
Working with binary files.
"""

my_bytes = b'This is a byte'

print(my_bytes[0])
print(my_bytes[0:2])

print(f"bytes(10) is {bytes(10)}")
print(f"bytes(range(10)) is {bytes(range(10))} \n")

# bytearray is a mutable object
print(f"bytearray(10) is {bytearray(10)}")
print(f"bytearray(range(10)) is {bytearray(range(10))}")
print(f"Another example is {bytearray(b'This are bytes')}")

my_bytes = bytearray(10)
# my_bytes[0] = b'a'    # This won't work
my_bytes[0:1] = b'a'
print(f"my_bytes are {my_bytes}")
my_bytes[0] = 0x10
print(f"my_bytes now are {my_bytes}")