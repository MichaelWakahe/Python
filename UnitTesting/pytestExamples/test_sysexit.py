import pytest

"""
Asserts that a certain exception is raised.

Execute the test function with "quiet" reporting mode as follows:

$ pytest -q test_sysexit.py

Sample courtesy of https://docs.pytest.org
"""

def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()