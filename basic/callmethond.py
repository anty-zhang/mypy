# -*- coding: utf-8 -*-


class Next(object):
    List = []

    def __init__(self, low, high):
        for num in range(low, high):
            self.List.append(num)

    def __call__(self, Nu):
        print '***Next __call__ run Nu:', Nu
        return self.List[Nu]


def test1():
    b = Next(1, 7)
    print b.List
    print b(2)

    """
    output:
        [1, 2, 3, 4, 5, 6]
        ***Next __call__ run Nu: 2
        3
    """


def test2():
    """
    __init__是初始化函数，在生成类的实例时执行。
    而__call__是模拟()的调用，需要在实例上应用，因此这个实例自然是已经执行过__init__了。
    你所举的后面那个例子：
    b = Next
    这并不是创建实例，而是将class赋给一个变量。因此后面使用b进行的操作都是对Next类的操作，
    那么其实就是：
    Next(1,7)
    print Next.List
    print Next(2)
    """
    b = Next
    b(1, 7)
    print b.List
    print b(2)
    """
    output:
        [1, 2, 3, 4, 5, 6]
        Traceback (most recent call last):
        TypeError: __init__() takes exactly 3 arguments (2 given)
    """

if __name__ == "__main__":
    test2()

