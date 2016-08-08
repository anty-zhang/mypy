# -*- coding: utf-8 -*-


def foo(x):
    print(x)


class StaticMethod(object):
    def __init__(self, function):
        print("__init__() called")
        self.f = function

    def __get__(self, instance, owner):
        print("\t__get__() called")
        print("\tINFO: self = %s, instance =%s, owner = %s" % (self, instance, owner))
        return self.f


class Class1(object):
    method = StaticMethod(foo)


if __name__ == '__main__':
    ins = Class1()
    print("ins = %s, Class1 = %s" % (ins, Class1))
    print("ins.method = %s, Class1.method = %s" % (ins.method, Class1.method))
    ins.method('abc')
    Class1.method('xyz')


    """
    输出：
__init__() called
ins = <__main__.Class1 object at 0xb773f74c>, Class1 = <class '__main__.Class1'>
	__get__() called
	INFO: self = <__main__.StaticMethod object at 0xb773f6ec>, instance =<__main__.Class1 object at 0xb773f74c>, owner = <class '__main__.Class1'>
	__get__() called
	INFO: self = <__main__.StaticMethod object at 0xb773f6ec>, instance =None, owner = <class '__main__.Class1'>
ins.method = <function foo at 0xb773425c>, Class1.method = <function foo at 0xb773425c>
	__get__() called
	INFO: self = <__main__.StaticMethod object at 0xb773f6ec>, instance =<__main__.Class1 object at 0xb773f74c>, owner = <class '__main__.Class1'>
abc
	__get__() called
	INFO: self = <__main__.StaticMethod object at 0xb773f6ec>, instance =None, owner = <class '__main__.Class1'>
xyz
    """