from __future__ import annotations

def nth_fibonacci_iterative(n, /): ...
def nth_fibonacci_recursive(n, /, *, f0=0, f1=1): ...
def nth_fibonacci_recursive_tail(n, /): ...

class Fibonacci:
    """
    A class that computes the Fibonacci numbers.
    """

    def __init__(self, first_n, /):
        pass
    def __iter__(self, /):
        """
        Implement iter(self).
        """
        ...

class FibonacciIterator:
    """
    An iterator that computes the Fibonacci numbers.
    """

    def __init__(self, i, ith, next, stop, /):
        pass
    def __next__(self, /):
        """
        Implement next(self).
        """
        ...
