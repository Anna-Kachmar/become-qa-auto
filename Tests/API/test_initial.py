def test_lists():
    assert [1,2,3] == [1,2,3]

def test_lists_fail():
    assert ['a',2,3] != [1,2,3]

def test_lists_ok():
    assert ['a',2,3] == ['a',2,3]


# python3 -m pytest
