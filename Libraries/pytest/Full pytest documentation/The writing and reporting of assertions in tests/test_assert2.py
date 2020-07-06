"""
Making use of context-sensitive comparisons
pytest has rich support for providing context-sensitive information when it encounters comparisons.
For example:
    pytest test_assert2.py
"""


def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2