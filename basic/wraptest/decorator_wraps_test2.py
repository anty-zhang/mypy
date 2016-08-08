# -*- coding: utf-8 -*-
import functools
import sys

debug_log = sys.stderr


def trace(func):
    if debug_log:
        @functools.wraps(func)
        def callf(*args, **kwargs):
            """A wrapper function."""
            debug_log.write('Calling function: {}\n'.format(func.__name__))
            res = func(*args, **kwargs)
            debug_log.write('Return value: {}\n'.format(res))
            return res
        return callf
    else:
        return func


@trace
def square(x):
  """Calculate the square of the given number."""
  return x * x


if __name__ == '__main__':
    print(square(3))
    print(square.__doc__)
    print(square.__name__)