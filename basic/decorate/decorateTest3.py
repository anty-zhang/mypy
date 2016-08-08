# -*- coding: utf-8 -*-

'''
    第三步：使用语法糖@来装饰函数
    示例3: 使用语法糖@来装饰函数，相当于“myfunc = deco(myfunc)
        但发现新函数只在第一次被调用，且原函数多调用了一次

    执行流程：1）在执行到@deco 时，会执行装饰函数deco(func)，而此时函数def myfunc()并不在内存中
        存储其函数地址，而是作为参数传递给deco(func)中的func参数.因此，自始至终func的地址，将代表
        def myfunc()函数的地址，即变量func的地址就是def myfunc()函数的地址.
        2）执行完装饰函数deco中的语句
        3）装饰函数只被执行一次，而被装饰函数在执行时，装饰函数并不会再执行
'''


def deco(func):
    print 'deco func address:', func
    print 'deco address:', deco
    print 'before myfunc() called.'
    func()
    print 'after myfunc() called.'
    return func


@deco    # 装饰的此时deco()就会被调用
def myfunc():
    print("myfunc() called.")


if __name__ == '__main__':
    print 'main myfunc address:', myfunc
    myfunc()
    myfunc()

'''
    result:
            deco func address: <function myfunc at 0x8d9eed4>
            deco address: <function deco at 0x8d9ee64>
            before myfunc() called.
            myfunc() called.
            after myfunc() called.
            main myfunc address: <function myfunc at 0x8d9eed4>
            myfunc() called.
            myfunc() called.
'''
