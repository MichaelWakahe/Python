"""
Test with:
    pytest test_one.py

If you want to see the output of the print statement as the test runs:
    pytest -s test_one.py

For more details, add -v or --verbose
"""


def test_passing():
    print("About to run test")
    assert (1, 2, 3) == (1, 2, 3)
