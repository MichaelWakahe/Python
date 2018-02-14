"""
This is an example of grouping multiple tests in a class

$ pytest -q test_class.py

Sample courtesy of https://docs.pytest.org
"""
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')