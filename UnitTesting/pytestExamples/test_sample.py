"""
A very basic test.

Sample courtesy of https://docs.pytest.org
"""
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5