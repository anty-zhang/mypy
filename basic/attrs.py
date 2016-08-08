# -*- coding: utf-8 -*-

"""
*attr() 系列函数
1.在操作ojb.attr时，就会调用*attr(obj, 'attr', ...)系列函数
2. hasattr Boolean类型:判断一个对象是否有一个特定的属性
3.getattr,setattr:取值和赋值对象相应属性
4.delattr:删除对象中的一个属性
"""


class MyClass(object):
    def __init__(self):
        self.foo = 100

    def __getattr__(self, item):
        print 'MyClass __getattr__ here'
        print 'item is:', item

if __name__ == "__main__":
    myInst = MyClass()
    # print(hasattr(myInst, 'foo'))
    # print(getattr(myInst, 'foo'))
    #
    # print (hasattr(myInst, 'bar'))
    # # print (getattr(myInst, 'bar'))   # AttributeError: 'MyClass' object has no attribute 'bar'
    #
    # print (getattr(myInst, 'bar', 'oops'))
    #
    # setattr(myInst, 'bar', 'my attr')     # ['bar', 'foo']
    # print '================================================='
    # print dir(myInst)
    #
    # print getattr(myInst, 'bar')
    #
    # delattr(myInst, 'foo')
    # print hasattr(myInst, 'foo')
    #
    # print '================================================='
    #
    # myInst.foo
    setattr(myInst, 'test', 123)
    print myInst.test


"""
output:
    True
    100
    MyClass __getattr__ here
    item is: bar
    True
    MyClass __getattr__ here
    item is: bar
    None
    =================================================
    MyClass __getattr__ here
    item is: __members__
    MyClass __getattr__ here
    item is: __methods__
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'bar', 'foo']
    my attr
    MyClass __getattr__ here
    item is: foo
    True
    =================================================
    MyClass __getattr__ here
    item is: foo

"""