# -*- coding: utf-8 -*-

'''
第二步：使用装饰函数在函数执行前和执行后分别附加额外功能
    示例2: 替换函数(装饰)
    装饰函数的参数是被装饰的函数对象，返回原函数对象
    装饰的实质语句: myfunc = deco(myfunc)

    执行流程：1）在执行myfun = deco(myfunc)时，会调用deco函数，并且func将保存myfunc函数的地址
        2）然后开始执行deco中的语句，被装饰函数myfunc也将被执行
        3）装饰函数deco只被执行一次，在后续的执行myfun()时，也仅仅执行被装饰函数，装饰函数将不再被执行
'''

def deco(func):  # 装饰函数， func是被装饰函数参数，func的地址是myfunc函数的地址
    print 'deco func:', func
    print 'before myfunc() called.'
    func()
    print 'after myfunc() called.'
    return func   # 返回被装饰函数对象


def myfunc():
    print("myfunc() called.")

if __name__ == '__main__':
    print 'debug myfunc:', myfunc
    myfun = deco(myfunc)   # 装饰函数只被调用一次

    myfun()
    myfun()

'''
run result:
    debug myfunc: <function myfunc at 0xb768a454>
    deco func: <function myfunc at 0xb768a454>
    before myfunc() called.
    myfunc() called.
    after myfunc() called.
    myfunc() called.
    myfunc() called.
'''
