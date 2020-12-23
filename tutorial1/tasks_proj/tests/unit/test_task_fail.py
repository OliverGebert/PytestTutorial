from tasks import Task

def test_task_equality():
    # different task should not be equal
    t1 = Task('sit there', 'brian', True, 21)
    t2 = Task('do something', 'okken', False, 12)
    assert t1 != t2

def test_dict_equality():
    # different tasks compared as dicts should not be equal
    t1_dict = Task('sit there', 'brian')._asdict()
    t2_dict = Task('sit there', 'brian')._asdict()
    assert t1_dict == t2_dict