"""
Run tests in a module:
    pytest test_example.py

Run tests in a directory
    pytest testing/

Run tests by keyword expressions
    pytest -k "MyClass and not method"

Run tests by node ids:
    To run a specific test within a module:
        pytest test_example.py::test_ok

    Another example specifying a test method in the command line:
        pytest test_mod.py::TestClass::test_method


Run tests by marker expressions
    pytest -m xfail test_example.py


Examples for modifying traceback printing:
    pytest --showlocals # show local variables in tracebacks
    pytest -l           # show local variables (shortcut)

    pytest --tb=auto    # (default) 'long' tracebacks for the first and last
                         # entry, but 'short' style for the other entries
    pytest --tb=long    # exhaustive, informative traceback formatting
    pytest --tb=short   # shorter traceback format
    pytest --tb=line    # only one line per failure
    pytest --tb=native  # Python standard library formatting
    pytest --tb=no      # no traceback at all


Run tests from packages
    pytest --pyargs pkg.testing
    This will import pkg.testing and use its filesystem location to find and run tests from.


Detailed summary report
    pytest -ra test_example.py
    The -r flag can be used to display a "short test summary info" at the end of the test session, making it easy in
    large test suites to get a clear picture of all failures, skips, xfails, etc.
    The -r options accepts a number of characters after it, with a used above meaning "all except passes".
        pytest -ra test_example.py
    The -r options accepts a number of characters after it, with 'a' used above meaning "all except passes".

    More than one character can be used, so for example to only see failed and skipped tests, you can execute:
        pytest -rfs test_example.py

    Here is the full list of available characters that can be used:
        f - failed
        E - error
        s - skipped
        x - xfailed
        X - xpassed
        p - passed
        P - passed with output
        a - all except pP
        A - all


Dropping to PDB (Python Debugger) on failures
    pytest allows one to drop into the PDB prompt via a command line option:
        pytest --pdb test_example.py

    Drop to PDB on first failure, then end test session
        pytest -x --pdb test_example.py

    Drop to PDB for first three failures
        pytest --pdb --maxfail=3 test_example.py

    pytest allows one to drop into the PDB prompt immediately at the start of each test via a command line option:
        pytest --trace test_example.py

Setting breakpoints
    To set a breakpoint in your code use the native Python import pdb;pdb.set_trace() call in your code and pytest
    automatically disables its output capture for that test:
        * Output capture in other tests is not affected.
        * Any prior test output that has already been captured and will be processed as such.
        * Output capture gets resumed when ending the debugger session (via the continue command).


Profiling test execution duration
    To get a list of the slowest 10 test durations:
        pytest --durations=10 test_example.py

Fault Handler
    New in version 5.0.
    The faulthandler standard module can be used to dump Python tracebacks on a segfault or after a timeout.


Creating JUnitXML format files
    To create result files which can be read by Jenkins or other Continuous integration servers, use this invocation:
        pytest --junitxml=path
    to create an XML file at 'path'.

"""
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    print("Test with mark 'xfail'")
    pass