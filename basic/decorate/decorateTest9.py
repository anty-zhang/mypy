# -*- coding: utf-8 -*-

"""
第九步：装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器

"""

from mylocker import *


class example:
    @lockhelper(mylocker)
    def myfunc(self):
        print(" myfunc() called.")

    """
        装饰步骤：
            1.装饰参数顺序mylocker,mylocker
            2.装饰函数顺序lockerex,lockerex
        执行流程：
            例如：a.myfunc2(1, 2)
            1.执行mylocker类中的acquire
            2.执行lockerex类中的acquire
            3.执行func(*args, **kwargs)
            4.执行lockerex类中的cls.unlock()
            5.执行mylocker类中的cls.unlock()
            6.返回func的值
    """
    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print(" myfunc2() called.")
        return a + b

if __name__=="__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    # print(a.myfunc2(3, 4))


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
        before __deco called.
        mylocker.acquire() called.
        before myfunc2 called.
        lockerex.acquire() called.
         myfunc2() called.
          lockerex.unlock() called.
        mylocker.unlock() called.
        3
"""