# -*- coding: utf-8 -*-

'''
第六步：对参数数量不确定的函数进行装饰
    示例6: 对参数数量不确定的函数进行装饰，
    参数用(*args, **kwargs)，自动适应变参和命名参数
'''


def deco(func):
    print 'debug deco address of func:', func

    def inner_deco(*args, **kwargs):
        print "before %s called." % func.__name__
        print '===args:', args
        print '===**kwargs:', kwargs
        print
        print 'debug inner_deco address of func:', func
        ret = func(*args, **kwargs)
        print"  after %s called. result: %s" % (func.__name__, ret)
        return ret
    print 'debug deco address of inner_deco:', inner_deco
    return inner_deco


@deco
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b

@deco
def myfunc2(a, b, c):
    print " myfunc2(%s,%s,%s) called." % (a, b, c)
    return a + b + c

if __name__ == '__main__':
    print 'main myfunc address:', myfunc
    myfunc(1, 2)
    myfunc2(3, 4, 5)


'''
    result:
        debug deco address of func: <function myfunc at 0xb765cb1c>
        debug deco address of inner_deco: <function inner_deco at 0xb765ced4>
        debug deco address of func: <function myfunc2 at 0xb765ce9c>
        debug deco address of inner_deco: <function inner_deco at 0xb7662614>
        main myfunc address: <function inner_deco at 0xb765ced4>
        before myfunc called.
        ===args: (1, 2)
        ===**kwargs: {}

        debug inner_deco address of func: <function myfunc at 0xb765cb1c>
         myfunc(1,2) called.
          after myfunc called. result: 3
        before myfunc2 called.
        ===args: (3, 4, 5)
        ===**kwargs: {}

        debug inner_deco address of func: <function myfunc2 at 0xb765ce9c>
         myfunc2(3,4,5) called.
          after myfunc2 called. result: 12
'''
