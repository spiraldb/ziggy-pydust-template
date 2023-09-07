from fibonacci import _lib


def test_fibonacci():
    impls = [
        _lib.nth_fibonacci_iterative,
        _lib.nth_fibonacci_recursive,
        _lib.nth_fibonacci_recursive_tail,
    ]
    for impl in impls:
        assert impl(9) == 34


def test_fubonacci_iterator():
    fibonacci = _lib.Fibonacci(10)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # As iterator
    fibonacci_iter = iter(fibonacci)
    for expected_item in expected:
        actual = next(fibonacci_iter)
        assert actual == expected_item

    # As list
    fibonacci_list = list(fibonacci)
    for actual, expected_item in zip(fibonacci_list, expected):
        assert actual == expected_item
