# -*- coding:utf-8 -*-

"""
改写后的 fab 函数通过返回 List 能满足复用性的要求，但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大，
如果要控制内存占用，最好不要用 List
来保存中间结果，而是通过 iterable 对象来迭代。例如，在 Python2.x 中，代码：
清单 3. 通过 iterable 对象来迭代
 for i in range(1000): pass
会导致生成一个 1000 个元素的 List，而代码：
 for i in xrange(1000): pass
则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。
利用 iterable 我们可以把 fab 函数改写为一个支持 iterable 的 class，以下是第三个版本的 Fab：
"""


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

if __name__ == '__main__':
    for n in Fab(5):
        print n