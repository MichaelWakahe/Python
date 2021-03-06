"""Use the Task type to show test failures."""
from ...src.tasks.api import Task


def test_task_equality():
    """Different tasks should not be equal."""
    t1 = Task('sit there', 'brian')
    t2 = Task('do something', 'james')
    assert t1 == t2


def test_dict_equality():
    """Different tasks compared as dicts should not be equal."""
    t1_dict = Task('make sandwich', 'mike')._asdict()
    t2_dict = Task('make sandwich', 'ann')._asdict()
    assert t1_dict == t2_dict
