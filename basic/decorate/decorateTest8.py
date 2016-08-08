# -*- coding: utf-8 -*-

"""
第八步：让装饰器带 类 参数
    示例8: 装饰器带类参数
"""


class locker:
    def __init__(self):
        print("locker.__init__() should be not called.")

    @staticmethod
    def acquire():
        print("locker.acquire() called.（这是静态方法）")

    @staticmethod
    def release():
        print("locker.release() called.（不需要对象实例）")

    def test(self):
        pass


def deco(cls):
    """
        cls 必须实现acquire和release静态方法
    """
    def inner_deco(func):
        def inner2_deco():
            print("before %s called [%s]." % (func.__name__, cls))
            cls.acquire()
            try:
                return func()
            finally:
                cls.release()
        return inner2_deco
    return inner_deco


@deco(locker)
def myfunc():
    print(" myfunc() called.")
    return 'ok'


if __name__ == '__main__':
    res = myfunc()
    print 'res=', res



'''
    result:
        before myfunc called [__main__.locker].
        locker.acquire() called.（这是静态方法）
         myfunc() called.
        locker.release() called.（不需要对象实例）
        res= ok
'''
