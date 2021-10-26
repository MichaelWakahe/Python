"""
The Fibonacci sequence is such that each number is the sum of the two preceding ones, starting from 0 and 1.
F(0) = 0; F(1) = 1
F(N) = F(N-1) + F(N-2)

A video explanation is here: https://youtu.be/P8Xa2BitN3I
"""

import inspect


def stack_depth():
    return len(inspect.getouterframes(inspect.currentframe())) - 1


def fib(n: int) -> int:
    """
    The inefficient way of running this.

    In a tree, the height is n, and the number of nodes can be up to 2^n, therefore a worst case runtime complexity of
    O(2^n). Space complexity is O(n).

    :param n:
    :return:
    """
    print("{indent}fibonacci({n})called".format(indent=" " * stack_depth(), n=n))
    if n < 2:
        return n

    return fib(n - 1) + fib(n - 2)


# print(fib(10))

"""
Dynamic Programming - top down.

Here is one memoization option, where the memo is outside the function.
"""

memo = {}


def fib2(n: int) -> int:
    """
    The worst case runtime for this is O(n). Space complexity is O(n).

    :param n:
    :return:
    """
    if n < 2:
        return n

    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]


print(f"fib2(10) is {fib2(10)}")


def fib3(n: int, memo2: dict = {}) -> int:
    """
    Another Dynamic Programming example without an external variable - top down.

    :param memo2:
    :param n:
    :return:
    """
    print("{indent}fibonacci({n}) called".format(indent=" " * stack_depth(), n=n))
    if n < 2:
        return n

    if n not in memo2:
        memo2[n] = fib3(n-1, memo2) + fib3(n-2, memo2)

    return memo2[n]


print(f"fib3(10) is {fib3(10)}")


def fib4(n: int) -> int:
    """
    This is Dynamic Programming with a bottom up approach. It has a time and space complexity of O(n).

    :param n:
    :return:
    """
    f = [0, 1]  # The first two numbers in the sequence

    for j in range(2, n+1):
        f.append(f[j-1] + f[j-2])

    return f[n]


print(f"fib4(10) is {fib4(10)}")


def fib5(n: int) -> int:
    """
    This is Dynamic Programming with a bottom up approach. It has a time complexity of O(n) and a space complexity of
    O(1).

    :param n:
    :return:
    """
    prev_v, next_v = 0, 1

    for j in range(2, n+1):
        prev_v, next_v = next_v, next_v + prev_v

    return next_v


print(f"fib5(10) is {fib5(10)}")
