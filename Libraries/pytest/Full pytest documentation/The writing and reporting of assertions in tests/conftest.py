"""
Defining your own explanation for failed assertions
It is possible to add your own detailed explanations by implementing the pytest_assertrepr_compare hook.
"""
from test_foocompare import Foo


def pytest_assertrepr_compare(op, left, right):
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]
