"""
Test as follows:
    pytest test_assert1.py::test_function
    pytest test_assert1.py::test_function2
    pytest test_assert1.py::test_zero_division
    pytest test_assert1.py::test_recursion_depth
    pytest test_assert1.py::test_match
    pytest test_assert1.py::test_f
"""
import pytest


#######################################
# Asserting with the assert statement
#######################################
def f():
    return 3


def test_function():
    assert f() == 4


def test_function2():
    assert 3 % 2 == 0, "value was odd, should be even"



#######################################
# Assertions about expected exceptions
########################################
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# If you need to have access to the actual exception info you may use:
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
    # excinfo is a ExceptionInfo instance, which is a wrapper around the actual exception raised. The main attributes
    # of interest are .type, .value and .traceback.


# You can pass a match keyword parameter to the context-manager to test that a regular expression matches on the string
# representation of an exception (similar to the TestCase.assertRaisesRegexp method from unittest):
def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()
    # The regexp parameter of the match method is matched with the re.search function, so in the above example
    # match='123' would have worked as well.


# Note that it is also possible to specify a “raises” argument to pytest.mark.xfail, which checks that the test is
# failing in a more specific way than just having any exception raised:
@pytest.mark.xfail(raises=IndexError)
def test_f():
    f()
# Using pytest.raises is likely to be better for cases where you are testing exceptions your own code is deliberately r
# aising, whereas using @pytest.mark.xfail with a check function is probably better for something like documenting
# unfixed bugs (where the test describes what “should” happen) or bugs in dependencies.
