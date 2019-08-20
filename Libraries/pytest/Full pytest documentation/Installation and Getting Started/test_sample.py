"""

Test it on command line as follows:
    pytest test_sample.py

"""


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
