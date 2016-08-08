# -*- coding:utf-8 -*-

"""
如何判断一个函数是否是一个特殊的 generator 函数？可以利用 isgeneratorfunction 判断：
清单 7. 使用 isgeneratorfunction 判断
 >>> from inspect import isgeneratorfunction
 >>> isgeneratorfunction(fab)
 True
要注意区分 fab 和 fab(5)，fab 是一个 generator function，而 fab(5) 是调用 fab 返回的一个 generator，好比类的定义和类的实例的区别：
清单 8. 类的定义和类的实例
 >>> import types
 >>> isinstance(fab, types.GeneratorType)
 False
 >>> isinstance(fab(5), types.GeneratorType)
 True
fab 是无法迭代的，而 fab(5) 是可迭代的：
 >>> from collections import Iterable
 >>> isinstance(fab, Iterable)
 False
 >>> isinstance(fab(5), Iterable)
 True
每次调用 fab 函数都会生成一个新的 generator 实例，各实例互不影响：
 >>> f1 = fab(3)
 >>> f2 = fab(5)
 >>> print 'f1:', f1.next()
 f1: 1
 >>> print 'f2:', f2.next()
 f2: 1
 >>> print 'f1:', f1.next()
 f1: 1
 >>> print 'f2:', f2.next()
 f2: 1
 >>> print 'f1:', f1.next()
 f1: 2
 >>> print 'f2:', f2.next()
 f2: 2
 >>> print 'f2:', f2.next()
 f2: 3
 >>> print 'f2:', f2.next()
 f2: 5
回页首
return 的作用
在一个 generator function 中，如果没有 return，则默认执行至函数完毕，如果在执行过程中 return，则直接抛出 StopIteration 终止迭代。
回页首
另一个例子
另一个 yield 的例子来源于文件读取。如果直接对文件对象调用 read() 方法，会导致不可预测的内存占用。好的方法是利用固定长度的缓冲区来不断读取文件内容。通过 yield，我们不再需要编写读文件的迭代类，就可以轻松实现文件读取：
清单 9. 另一个 yield 的例子

以上仅仅简单介绍了 yield 的基本概念和用法，yield 在 Python 3 中还有更强大的用法，我们会在后续文章中讨论。
注：本文的代码均在 Python 2.7 中调试通过

"""


def read_file(fpath):
    BLOCK_SIZE = 1024
    with open(fpath, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

if __name__ == '__main__':
    for i in read_file('/home/andy/568a0ff70adb7.jpg'):
        print i