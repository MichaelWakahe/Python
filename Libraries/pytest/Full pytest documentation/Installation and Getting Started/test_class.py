"""

This is an example of grouping multiple tests in a class

To execute it:
    pytest -q test_class.py

"""
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')