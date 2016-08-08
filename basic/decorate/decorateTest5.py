# -*- coding: utf-8 -*-

'''
第五步：对带参数的函数进行装饰
    示例5: 对带参数的函数进行装饰，
        内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象

    执行流程:同decorateTest4.py，只是带了参数的不同而已
'''


def deco(func):
    print 'debug deco address of func:', func

    def inner_deco(a, b):
        print("before myfunc() called.")
        print 'debug inner_deco address of func:', func
        ret = func(a, b)
        print("  after myfunc() called. result: %s" % ret)
        return ret
    print 'debug deco address of inner_deco:', inner_deco
    return inner_deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b


if __name__ == '__main__':
    print 'main myfunc address:', myfunc
    myfunc(1, 2)
    myfunc(3, 4)
    pass

'''
    result:
        debug deco address of func: <function myfunc at 0x9a95f7c>
        debug deco address of inner_deco: <function inner_deco at 0x9a95fb4>
        main myfunc address: <function inner_deco at 0x9a95fb4>
        before myfunc() called.
        debug inner_deco address of func: <function myfunc at 0x9a95f7c>
         myfunc(1,2) called.
          after myfunc() called. result: 3
        before myfunc() called.
        debug inner_deco address of func: <function myfunc at 0x9a95f7c>
         myfunc(3,4) called.
          after myfunc() called. result: 7
'''
