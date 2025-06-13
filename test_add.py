from main import plus_one

def test_plus_one():
    assert plus_one(1) == 2
    assert plus_one(0) == 1
    assert plus_one(-1) == 0