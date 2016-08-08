# -*- coding:utf-8 -*-


""""
url:http://luozhaoyu.iteye.com/blog/1506426

__get__,__getattr__和__getattribute都是访问属性的方法，但不太相同。
object.__getattr__(self, name)
当一般位置找不到attribute的时候，会调用getattr，返回一个值或AttributeError异常。

object.__getattribute__(self, name)
无条件被调用，通过实例访问属性。如果class中定义了__getattr__()，则__getattr__()不会被调用
（除非显示调用或引发AttributeError异常）

object.__get__(self, instance, owner)
如果class定义了它，则这个class就可以称为descriptor。owner是所有者的类，instance是访问descriptor的实例，
如果不是通过实例访问，而是通过类访问的话，instance则为None。（descriptor的实例自己访问自己是
不会触发__get__，而会触发__call__，只有descriptor作为其它类的属性才有意义。）
（所以下文的d是作为C2的一个属性被调用）

"""


class C(object):
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        return object.__getattribute__(self, *args, **kwargs)
#        return "haha"

    def __getattr__(self, name):
        print("__getattr__() is called ")
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)
        return self

    def foo(self, x):
        print(x)


class C2(object):
    d = C()


if __name__ == '__main__':
    c = C()
    c2 = C2()
    """print(c.zzzzzzzz)
    c2.d
    print(c2.d.a)
    print(c.a)
    print(c.zzzzzzzz)
    """
    c2.d
    # print(c2.d.a)




"""
output:
__getattribute__() is called
abc
__getattribute__() is called
__getattr__() is called
zzzzzzzz from getattr
('__get__() is called', <__main__.C2 object at 0xb76af6ec>, <class '__main__.C2'>)
('__get__() is called', <__main__.C2 object at 0xb76af6ec>, <class '__main__.C2'>)
__getattribute__() is called
abc

小结：可以看出，每次通过实例访问属性，都会经过__getattribute__函数。而当属性不存在时，
仍然需要访问__getattribute__，不过接着要访问__getattr__。这就好像是一个异常处理函数。
每次访问descriptor（即实现了__get__的类），都会先经过__get__函数。

需要注意的是，当使用类访问不存在的变量是，不会经过__getattr__函数。
而descriptor不存在此问题，只是把instance标识为none而已。

"""