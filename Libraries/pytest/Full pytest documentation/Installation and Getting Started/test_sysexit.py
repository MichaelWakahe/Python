import pytest

"""
Asserts that a certain exception is raised. Use the raises helper to assert that some code raises an exception.

Execute the test function with "quiet" reporting mode as follows:

    pytest -q test_sysexit.py
"""


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()