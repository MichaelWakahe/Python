"""
Asserting with the assert statement

To run example:
    pytest test_assert1.py
"""


def f():
    return 3


def test_function():
    #assert f() == 4
    assert 3 % 2 == 0, "value was odd, should be even"