# -*- coding: utf-8 -*-
"""
    mylocker.py: 公共类 for 示例9.py
"""


class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")
         
    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")
         
    @staticmethod
    def unlock():
        print("mylocker.unlock() called.")


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")
         
    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):
    """
        cls 必须实现acquire和release静态方法
    """
    def inner_deco(func):
        def inner2_deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()
        return inner2_deco
    return inner_deco

"""
    result:
        before myfunc called.
        mylocker.acquire() called.
         myfunc() called.
        mylocker.unlock() called.
        before myfunc called.
        mylocker.acquire() called.
         myfunc() called.
        mylocker.unlock() called.
        None
        before inner2_deco called.
        mylocker.acquire() called.
        before myfunc2 called.
        lockerex.acquire() called.
         myfunc2() called.
          lockerex.unlock() called.
        mylocker.unlock() called.
        3
"""