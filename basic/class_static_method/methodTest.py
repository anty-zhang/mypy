# -*- coding: utf-8 -*-


class Human(object):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight


class Human1(object):
    weight = 40

    @classmethod
    def get_weight(cls):
        return cls.weight


class Human2(object):
    @staticmethod
    def add(a, b):
        return a + b

    def get_weight(self):
        return self.add(1, 2)

if __name__ == '__main__':
    print Human.get_weight    # <unbound method Human.get_weight>
    # print Human.get_weight()
    """
    output for Human.get_weight() :
    File "/home/andy/Documents/documents/python/basic/methodTest.py", line 13, in <module>
    print Human.get_weight()
        TypeError: unbound method get_weight() must be called with Human instance as first argument (got nothing instead)
    """
    print Human.get_weight(Human(45))  # 未绑定的方法必须使用一个Human实例作为第一个参数来调用啊。那我们来试试

    person = Human(45)            # 一般情况下我们习惯这么使用
    print person.get_weight()     # 一般情况下我们习惯这么使用
    print person.get_weight       # <bound method Human.get_weight of <__main__.Human object at 0xb77515ac>>

    """
        总结下
            instance method 就是实例对象与函数的结合。
            使用类调用，第一个参数明确的传递过去一个实例。
            使用实例调用，调用的实例被作为第一个参数被隐含的传递过去。
    """

    print '========test class method============'
    print Human1.get_weight    # <bound method type.get_weight of <class '__main__.Hunman1'>>
    """
        类和类的实例都能调用 get_weight 而且调用结果完全一样。
        我们看到 weight 是属于 Human 类的属性，当然也是 Human 的实例的属性。那传递过去的参数 cls 是类还是实例呢？
        我们看到传递过去的都是 Human 类,不是 Human 的实例，两种方式调用的结果没有任何区别。cls 只是一个普通的函数参数，调用时被隐含的传递过去。
        总结起来
        class_static_method 是类对象与函数的结合。
        可以使用和类的实例调用，但是都是将类作为隐含参数传递过去。
        使用类来调用 class_static_method 可以避免将类实例化的开销。
    """
    print Human1.get_weight()
    print Human1().get_weight()
    print Human1.get_weight       # <bound method type.get_weight of <class '__main__.Human1'>>
    print Human1().get_weight     # <bound method type.get_weight of <class '__main__.Human1'>>

    print '==========test statistics method============='
    """
        add 在两个实例上也是同一个对象。instancemethod 就不一样了，每次都会创建一个新的 get_weight 对象。
        总结下
        当一个函数逻辑上属于一个类又不依赖与类的属性的时候，可以使用staticmethod。
        使用 staticmethod 可以避免每次使用的时都会创建一个对象的开销。
        staticmethod 可以使用类和类的实例调用。但是不依赖于类和类的实例的状态。
    """
    print Human2.add          # <function add at 0xb7674e9c>
    print Human2().add        # <function add at 0xb7674e9c>
    print Human2().add is Human2().add         # true
    print Human2().get_weight is Human2().get_weight   # false



"""
    Python方法间调用，self.方法跟cls=类名;cls.方法，二种方式有什么区别？
    我看到tornado有个聊天室的demo，类MessageMixin的方法间调用使用了cls=类;cls.方法的方式，自己改成self.方法似乎跟之前的调用方式没有区别，不知道这两种方式是不是有什么深层的不同？

    什么是method？
    function就是可以通过名字可以调用的一段代码,我们可以传参数进去，得到返回值。所有的参数都是明确的传递过去的。
    method是function与对象的结合。我们调用一个方法的时候，有些参数是隐含的传递过去的。下文会详细介绍。
    instancemethod
    In [5]: class Human(object):
       ...:     def __init__(self, weight):
       ...:         self.weight = weight
       ...:     def get_weight(self):
       ...:         return self.weight
       ...:

    In [6]: Human.get_weight
    Out[6]: <unbound method Human.get_weight>
    这告诉我们get_weight是一个没有被绑定方法，什么叫做未绑定呢？继续看下去。
    In [7]: Human.get_weight()
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    /home/yao/learn/insight_python/<ipython-input-7-a2b2c5cd2f8d> in <module>()
    ----> 1 Human.get_weight()

    TypeError: unbound method get_weight() must be called with Human instance as first argument (got nothing instead)
    未绑定的方法必须使用一个Human实例作为第一个参数来调用啊。那我们来试试
    In [10]: Human.get_weight(Human(45))
    Out[10]: 45
    果然成功了，但是一般情况下我们习惯这么使用。
    In [11]: person = Human(45)

    In [12]: person.get_weight()
    Out[12]: 45
    这两种方式的结果一模一样。我们看下官方文档是怎么解释这种现象的。
    When an instance attribute is referenced that isn’t a data attribute, its class is searched.
    If the name denotes a valid class attribute that is a function object, a method object is
    created by packing (pointers to) the instance object and the function object just found together
    in an abstract object: this is the method object. When the method object is called with an
    argument list, a new argument list is constructed from the instance object and the argument list,
    and the function object is called with this new argument list.
    原来我们常用的调用方法(person.get_weight())是把调用的实例隐藏的作为一个参数self传递过去了, self 只是一个普通的参数名称,不是关键字。
    In [13]: person.get_weight
    Out[13]: <bound method Human.get_weight of <__main__.Human object at 0x8e13bec>>

    In [14]: person
    Out[14]: <__main__.Human at 0x8e13bec>
    我们看到get_weight被绑定在了 person 这个实例对象上。
    总结下
    instance method 就是实例对象与函数的结合。
    使用类调用，第一个参数明确的传递过去一个实例。
    使用实例调用，调用的实例被作为第一个参数被隐含的传递过去。
    class_static_method
    In [1]: class Human(object):
       ...:     weight = 12
       ...:     @class_static_method
       ...:     def get_weight(cls):
       ...:         return cls.weight

    In [2]: Human.get_weight
    Out[2]: <bound method type.get_weight of <class '__main__.Human'>>
    我们看到get_weight是一个绑定在 Human 这个类上的method。调用下看看
    In [3]: Human.get_weight()
    Out[3]: 12
    In [4]: Human().get_weight()
    Out[4]: 12
    类和类的实例都能调用 get_weight 而且调用结果完全一样。
    我们看到 weight 是属于 Human 类的属性，当然也是 Human 的实例的属性。那传递过去的参数 cls 是类还是实例呢？
    In [1]: class Human(object):
       ...:     weight = 12
       ...:     @class_static_method
       ...:     def get_weight(cls):
       ...:         print cls

    In [2]: Human.get_weight()
    <class '__main__.Human'>

    In [3]: Human().get_weight()
    <class '__main__.Human'>
    我们看到传递过去的都是 Human 类,不是 Human 的实例，两种方式调用的结果没有任何区别。cls 只是一个普通的函数参数，调用时被隐含的传递过去。
    总结起来
    class_static_method 是类对象与函数的结合。
    可以使用和类的实例调用，但是都是将类作为隐含参数传递过去。
    使用类来调用 class_static_method 可以避免将类实例化的开销。
    staticmethod
    In [1]: class Human(object):
       ...:     @staticmethod
       ...:     def add(a, b):
       ...:         return a + b
       ...:     def get_weight(self):
       ...:         return self.add(1, 2)

    In [2]: Human.add
    Out[2]: <function __main__.add>

    In [3]: Human().add
    Out[3]: <function __main__.add>

    In [4]: Human.add(1, 2)
    Out[4]: 3

    In [5]: Human().add(1, 2)
    Out[5]: 3
    我们看到 add 在无论是类还是实例上都只是一个普通的函数，并没有绑定在任何一个特定的类或者实例上。可以使用类或者类的实例调用，并且没有任何隐含参数的传入。
    In [6]: Human().add is Human().add
    Out[6]: True

    In [7]: Human().get_weight is Human().get_weight
    Out[7]: False
    add 在两个实例上也是同一个对象。instancemethod 就不一样了，每次都会创建一个新的 get_weight 对象。
    总结下
    当一个函数逻辑上属于一个类又不依赖与类的属性的时候，可以使用staticmethod。
    使用 staticmethod 可以避免每次使用的时都会创建一个对象的开销。
    staticmethod 可以使用类和类的实例调用。但是不依赖于类和类的实例的状态。
"""