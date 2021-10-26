"""
Bit manipulation examples.

Python bitwise operators work only on integers.

OPERATOR	    DESCRIPTION	                SYNTAX
&	            Bitwise AND	                x & y
|	            Bitwise OR	                x | y
~	            Bitwise NOT	                ~x
^	            Bitwise XOR	                x ^ y
>>	            Bitwise right shift	        x>>
<<	            Bitwise left shift	        x<<
"""

print(f"bin(8) is {bin(8)}")
print(f"bin(7) is {bin(7)}")
print(f"bin(32) is {bin(32)}")
print(f"bin(31) is {bin(31)}\n")


def dec_to_bin(x: int) -> str:
    """
    A function to manually convert decimal numbers to binary.
    """
    bin_str = ""

    num, remainder = x, 0

    while num:
        remainder, num = num % 2, num // 2
        bin_str = bin_str + str(remainder)

    bin_str = bin_str[::-1]  # Reverse the string
    return bin_str


print(f"bin(47) is {bin(47)}\n")
assert dec_to_bin(47) == "101111"


def binary_to_decimal(val: str) -> int: return int(val, 2)


print(f"binary_to_decimal(1010) is {binary_to_decimal('1010')}")
print(f"bin(10) is {bin(10)}")  # 0b1010
a = 10
"""
Bitwise not operator: Returns one’s complement of the number.

The '~' operator invert all bits of integer but we can't see native result because all integers in Python have signed 
representation.

~a = ~1010
   = -(1010 + 1)
   = -(1011)
   = -11 (Decimal)
"""
assert ~a == -11
assert ~a == -0b1011


a = 0b1011
b = 0b0101
assert a | b == 0b1111
assert a & b == 0b1
assert a ^ b == 0b1110

a = 10  # 0b1010
print(f"bin(a) is {bin(a)}")
assert a & a == a
assert a | a == a
assert a ^ a == 0
assert a << 1 == a * 2      # 'a << n' is equivalent to 'a * 2^n'
assert a >> 1 == a // 2     # 'a >> n' is equivalent to 'a // 2^n' (floor division)
print(f"{bin(a)} << 1 is {bin(a << 1)}")
print(f"{bin(a)} >> 1 is {bin(a >> 1)}\n")


def is_power_of_two(x): return (x != 0) and ((x & (x - 1)) == 0)


assert is_power_of_two(8)
assert not is_power_of_two(9)
