from tasks_package import package_func

def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_failing():
    assert (1, 2) == (1, 2)

def test_tasks_func():
    assert package_func() == 42
