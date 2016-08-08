# -*- coding: utf-8 -*-

# http://luozhaoyu.iteye.com/blog/1506376


def foo2(cls, x):
    print("foo2's class = ", cls)
    print(x)


class ClassMethod(object):
    def __init__(self, function):
        print("ClassMethod: __init__() called")
        self.f = function

    def __get__(self, instance, owner = None):
        print("\t__get__() called")
        print("\tINFO: self = %s, instance =%s, owner = %s" % (self, instance, owner))

        def tmpfunc(x):
            print("I'm tmpfunc")
            return self.f(owner, x)
        return tmpfunc


class Class2(object):
    method = ClassMethod(foo2)


class Class21(Class2):
    pass
if __name__ == '__main__':
    ins = Class2()
    print("ins.method = %s, Class2.method = %s, Class21.method = %s" % (ins.method, Class2.method, Class21.method))
    ins.method('abc')
    Class2.method('xyz')
    Class21.method('asdf')


"""
    output:
    ClassMethod: __init__() called
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =<__main__.Class2 object at 0xb771b8cc>, owner = <class '__main__.Class2'>
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =None, owner = <class '__main__.Class2'>
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =None, owner = <class '__main__.Class21'>
ins.method = <function tmpfunc at 0xb77107d4>, Class2.method = <function tmpfunc at 0xb7710ed4>, Class21.method = <function tmpfunc at 0xb7710e9c>
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =<__main__.Class2 object at 0xb771b8cc>, owner = <class '__main__.Class2'>
I'm tmpfunc
("foo2's class = ", <class '__main__.Class2'>)
abc
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =None, owner = <class '__main__.Class2'>
I'm tmpfunc
("foo2's class = ", <class '__main__.Class2'>)
xyz
	__get__() called
	INFO: self = <__main__.ClassMethod object at 0xb771b86c>, instance =None, owner = <class '__main__.Class21'>
I'm tmpfunc
("foo2's class = ", <class '__main__.Class21'>)
asdf

"""