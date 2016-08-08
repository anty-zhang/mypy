# -*- coding:utf-8 -*-

"""
https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
"""


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    fab(5)