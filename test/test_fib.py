from fibonacci import _lib

def test_fibonacci():
    assert _lib.get_fibonacci(9) == 34
