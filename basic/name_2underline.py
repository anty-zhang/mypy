# -*- coding: utf-8 -*-


class A(object):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print 'A.__private()'

    def public(self):
        print 'A.public()'


class B(A):
    """
    def __init__(self):
        self.__private()
        self.public()

    """

    def __private(self):
        print 'B.__private()'

    def public(self):
        print 'B.public()'


if __name__ == '__main__':
    b = B()

    """
    output:
        A.__private()
        B.public()
    """


"""
原文：http://blog.csdn.net/carolzhang8406/article/details/6859480

>>> from name_2underline import A,B
>>> dir(A)
['_A__private', '__init__', 'public']
>>>
>>> dir(B)
['_A__private', '_B__private', '__init__', 'public']
>>>
======>为什么类A有个名为_A__private的 Attribute 呢？而且__private消失了！
这就要谈谈Python的私有变量轧压了
私有变量会在代码生成之前被转换为长格式（变为公有）。
转换机制是这样的：在变量前端插入类名，再在前端加入一个下划线字符。
这就是所谓的私有变量轧压（Private name mangling）。
如类 A里的__private标识符将被转换为_A__private，这就是上一节出现_A__private和__private消失的原因了。


再讲两点题外话：
一是因为轧压会使标识符变长，当超过255的时候，Python会切断，要注意因此引起的命名冲突。
二是当类名全部以下划线命名的时候，Python就不再执行轧压。如：
>>> class ____(object):
       def __init__(self):
              self.__method()
       def __method(self):
              print '____.__method()'
>>> print '\n'.join(dir(____))
__class__
__delattr__
__dict__
__doc__
__getattribute__
__hash__
__init__
__method              # 没被轧压
__module__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__str__
__weakref__
>>> obj = ____()
____.__method()
>>> obj.__method()      # 可以外部调用
____.__method()

1.Python把以两个或以上下划线字符开头且没有以两个或以上下划线结尾的变量当作私有变量

"""