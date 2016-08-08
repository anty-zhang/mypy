# -*- coding: utf-8 -*-

'''
第四步：使用内嵌包装函数来确保每次新函数都被调用
    示例4: 使用内嵌包装函数来确保每次新函数都被调用
        内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象

    通过此流程看出装饰器的实质
    执行流程：1）在执行到@deco装饰器代码时，会调用装饰器函数def deco(func)，此时生成的形参变量func地址
        将是被装饰函数myfunc()的地址.包装函数内func的操作，实际上是被包装函数的操作.
        2）然后执行装饰函数中的内嵌包装函数inner_deco()[内嵌包装函数内部的代码，此时将不会被执行]，
        并将地址返回，最后会将其地址赋值给被装饰函数变量myfunc，即此时的被装饰函数myfunc的地址将是
        内嵌装饰函数inner_deco的地址.
        3）在main函数中执行myfunc()函数时，实际上执行的内嵌包装函数inner_deco()
'''


def deco(func):   # (2) func
    print 'debug deco address of func:', func

    def inner_deco():
        print 'before myfunc() called.'
        print 'debug _deco address of func:', func
        tt = func()
        print 'tt:', tt
        print 'after myfunc() called.'
        # 不需要返回func，实际上应返回原函数的返回值

    print 'debug deco address of _deco:', inner_deco
    return inner_deco   # 装饰函数返回内嵌包装函数对象


# 装饰的此时deco()就会被调用, 只有在每次调用myfunc函数时，装饰器才会调用
@deco
def myfunc():
    print("myfunc() called.")
    return 'ok'


if __name__ == '__main__':
    print 'main myfunc address:', myfunc
    myfunc()
    myfunc()


'''
    result:
        debug deco address of func: <function myfunc at 0x9c20f44>
        debug deco address of _deco: <function inner_deco at 0x9c20f7c>
        main myfunc address: <function inner_deco at 0x9c20f7c>
        before myfunc() called.
        debug _deco address of func: <function myfunc at 0x9c20f44>
        myfunc() called.
        tt: ok
        after myfunc() called.
        before myfunc() called.
        debug _deco address of func: <function myfunc at 0x9c20f44>
        myfunc() called.
        tt: ok
        after myfunc() called.
'''
