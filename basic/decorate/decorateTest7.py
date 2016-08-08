# -*- coding: utf-8 -*-

"""
第七步：让装饰器带参数
    示例7: 在示例4的基础上，让装饰器带参数，
    和上一示例相比在外层多了一层包装。
    装饰函数名实际上应更有意义些

    执行流程：1）第一次装饰参数：在执行@deco("mymodule1")时，首先调用装饰函数deco(arg)，将参数arg赋值为mymodule1
                再将第一层内嵌装饰函数inner_deco(func)的地址返回
        2）第二次装饰函数：然后再调用第一层返回的内嵌装饰函数，后面的执行流程同decorateTest4.py
"""


def deco(arg):
    print 'debug deco address of func:', arg

    def inner_deco(func):
        print 'inner_deco func address:', func, ' ,arg is:', arg

        def inner2_deco():
            print "before %s called." % func.__name__

            print 'debug inner_deco address of func:', func
            func()
            print"  after %s called." % func.__name__
            print 'debug deco address of inner_deco2:', inner2_deco
        print 'inter_deco2 address:', inner2_deco
        return inner2_deco
    print 'debug deco address of inner_deco:', inner_deco
    return inner_deco


def cache_func_result(key_func, timeout):
    print '=========== out wrapper key_func:', key_func, 'timeout:', timeout
    def wrapper(func):
        print '++++++++ in wrapper func is:', func
        def inner_func(*args):
            print '---------into inner_func args:', args
            print '---------into inner_func key_func:', key_func
            print '---------into inner_func func:', func

            key = key_func(*args)
            # result = cache.get(key)
            # if not result:
            result = func(*args)
            # cache.set(key, result, timeout=timeout)
            return result
        print '++++++++ in wrapper func is:', inner_func
        return inner_func
    print '===========out wrapper:', wrapper, ' end================'
    return wrapper


@cache_func_result(lambda category: 'category_list:%s' % category, 200)
def test_cache_func_deco(category):
    app_bar_list = []
    appbar_dict = {}
    appbar_dict['bar_name'] = 'name'
    appbar_dict['jump_address'] = 'address'
    appbar_dict['bar_interface'] = 'interface'
    appbar_dict['sorted_index'] = 10
    app_bar_list.append(appbar_dict)
    return app_bar_list

print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
@deco("mymodule1")
def myfunc():
    print("myfunc called.")


'''
@deco('mymodule2')
def myfunc2():
    print("myfunc2 called.")
'''

if __name__ == '__main__':
    # print 'main myfunc address:', myfunc
    # myfunc()

    print '$$$$$$$$$$$$$$$$$$main$$$$$$$$$$$$$$$$$$$$$$$$$$'
    print '__main__ name test_cache_func_deco addresss:', test_cache_func_deco
    test_cache_func_deco('zuixin')
    pass



'''
    result:
        debug deco address of func: mymodule1
        debug deco address of inner_deco: <function inner_deco at 0x94d5fb4>
        inner_deco func address: <function myfunc at 0x94dc02c>
        inter_deco2 address: <function inner2_deco at 0x94dc064>
        main myfunc address: <function inner2_deco at 0x94dc064>
        before myfunc called.
        debug inner_deco address of func: <function myfunc at 0x94dc02c>
        myfunc called.
          after myfunc called.
        debug deco address of inner_deco2: <function inner2_deco at 0x94dc064>
'''
