# -*- coding: utf-8 -*-
"""
http://www.tuicool.com/articles/2maEVr
我们定义了一个装饰器trace，用于追踪函数的调用过程及函数调用的返回值
"""
import sys

debug_log = sys.stderr


def trace(func):
    if debug_log:
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


def no_square(x):
    # 不使用装饰器
    return x * x

if __name__ == '__main__':
    # 使用装饰器
    print(square(3))

    # 不使用装饰器
    # print '==========================='
    # square = trace(no_square)
    # print square(4)
