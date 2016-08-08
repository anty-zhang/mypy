本文源于一时好奇，想要弄清出python的staticmethod()这一builtin方法的实现，查了一些资料（主要是python官方手册了）汇集于此

python在类中，有三种调用method的方法：普通method，staticmethod和classmethod
前两个应该都好理解，classmethod就是在调用这个函数的时候，会把调用对象的class object对象隐式地传进去。咦？这个class object不是一个类型？No，在python里面，class object不像静态语言一样是个类型，它在虚拟机中，就是一个对象
普通method调用需要把自己self作为参数传递，初学的时候怎么着也不能理解，不过看多了就自然熟悉了。比较奇怪的是staticmethod和classmethod不像静态语言一样，通过保留关键字定义，而是使用@staticmethod或者staticmethod()这种builtin函数进行定义。这个@staticmethod到底是个什么东东？
Python代码  收藏代码

    @staticmethod
    def foo(x):
        print(x)



之前用过java，所以第一反应这是个annotation……唔，确实感觉像个AOP的东西，python里把它称作decorator。如果我们要自己实现一个staticmethod，该怎么写呢？

研究了下官方的代码，我再改了改，感觉应该这样写：
Python代码  收藏代码

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



输出结果是：
Python代码  收藏代码

    __init__() called
    ins = <__main__.Class1 object at 0xece2d0>, Class1 = <class '__main__.Class1'>
        __get__() called
        INFO: self = <__main__.StaticMethod object at 0xece5d0>, instance =<__main__.Class1 object at 0xece2d0>, owner = <class '__main__.Class1'>
        __get__() called
        INFO: self = <__main__.StaticMethod object at 0xece5d0>, instance =None, owner = <class '__main__.Class1'>
    ins.method = <function foo at 0xeb6c00>, Class1.method = <function foo at 0xeb6c00>
        __get__() called
        INFO: self = <__main__.StaticMethod object at 0xece5d0>, instance =<__main__.Class1 object at 0xece2d0>, owner = <class '__main__.Class1'>
    abc
        __get__() called
        INFO: self = <__main__.StaticMethod object at 0xece5d0>, instance =None, owner = <class '__main__.Class1'>
    xyz


嗯，看上去一切都挺顺利，Class1包含了一个变量method，不过这个method其实也是一个特殊处理过的StaticMethod类。这个类中有一个__get__函数，当类被“get”的时候，被访问的时候，会默认把访问者的instance和class信息都传进来。所以我们看到不管是否调用method()这个函数，只要碰着了method，这个函数就会触发，就会打印出当前instance和class信息。虽然ins和Class1的instance各有不同，但__get__函数中只是返回foo函数，所以这里调用method之时就没有区别，调用的都是同一个function对象。

好的，那么classmethod又如何实现呢？
Python代码  收藏代码

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



输出结果是：
Python代码  收藏代码

    ClassMethod: __init__() called
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =<__main__.Class2 object at 0xdeb350>, owner = <class '__main__.Class2'>
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =None, owner = <class '__main__.Class2'>
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =None, owner = <class '__main__.Class21'>
    ins.method = <function tmpfunc at 0xdee050>, Class2.method = <function tmpfunc at 0xdee1e8>, Class21.method = <function tmpfunc at 0xdee270>
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =<__main__.Class2 object at 0xdeb350>, owner = <class '__main__.Class2'>
    I'm tmpfunc
    foo2's class =  <class '__main__.Class2'>
    abc
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =None, owner = <class '__main__.Class2'>
    I'm tmpfunc
    foo2's class =  <class '__main__.Class2'>
    xyz
        __get__() called
        INFO: self = <__main__.ClassMethod object at 0xdeb250>, instance =None, owner = <class '__main__.Class21'>
    I'm tmpfunc
    foo2's class =  <class '__main__.Class21'>
    asdf



可以看出，classmethod和staticmethod的实现方法是大同小异。staticmethod比较简单，直接返回self.f变量就好了，而classmethod不行，需要把调用时候的class类型信息传给foo2函数，这个函数根据接收的class信息来作不同的工作。（不过我现在也没有想到可以用来做些什么）

有个地方值得注意，可能同志们刚才也已经想到了，我一定必须要定义一个tempfunc，再返回它才能完成工作吗？可不可以不要
Java代码  收藏代码

    def tmpfunc(x):
                print("I'm tmpfunc")
                return self.f(owner, x)
            return tmpfunc



而直接返回一个
Java代码  收藏代码

    return self.f(owner, *args)


？

我刚试了一把，直接传args默认参数是不行的，因为__get__被调用的时候，还没有把参数传进来。只有return tmpfunc之后，Class2.method('xyz')的参数才挂在tmpfunc之上。

当然，如果有朋友成功做到了，请一定留言告诉我XD

小结：看来staticmethod和classmethod实现不是很困难，多亏了__get__函数帮忙。前文也提到__get__被调用时会把instance和class信息都填进来，真是帮了很大忙。但是，这个__get__函数到底又是怎么一回事？为什么这么神奇？这里卖个关子，本文先不讲了，下篇博文再看看这个__get__函数吧