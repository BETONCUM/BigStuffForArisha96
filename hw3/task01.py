"""
##In previous homework task 4, you wrote a cache function that remembers other function output value.

Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


#Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from functools import wraps
from collections import Callable


def cache(times: int) -> Callable:
    def decorator(func):
        cached_results = {}
        remaining_times = times

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal remaining_times

            # Convert args and kwargs into a hashable key
            key = (args, frozenset(kwargs.items()))

            # If the result for the key is already in cache and there are remaining times, return it
            if key in cached_results and remaining_times > 0:
                remaining_times -= 1
                return cached_results[key]

            # Invoke the original function and store the result in cache
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

        return wrapper

    return decorator
