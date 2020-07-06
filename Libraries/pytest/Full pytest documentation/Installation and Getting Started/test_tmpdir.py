"""
pytest provides Builtin fixtures/function arguments to request arbitrary resources, like a unique temporary directory.

List the name tmpdir in the test function signature and pytest will lookup and call a fixture factory to create the
resource before performing the test function call. Before the test runs, pytest creates a unique-per-test-invocation
temporary directory.

Test this functionality by repeatedly running the command below. Observe the output of the print.
    pytest -q test_tmpdir.py
"""


def test_needsfiles(tmpdir):
    print(tmpdir)
    assert 0