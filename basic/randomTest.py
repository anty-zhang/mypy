# -*- coding: utf-8 -*-

"""
Python中的random模块用于生成随机数，记录下来，方便以后查询使用
1.random.random()用于生成一个0到1的随机符点数: 0 <= n < 1.0
2.random.uniform(a, b)用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，
一个是下限。如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a。
3.random.randint(a, b)，用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，
生成的随机数n: a <= n <= b
4.random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中
获取一个随机数。如：random.randrange(10, 100, 2)，结果相当于从
[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数。random.randrange(10, 100, 2)
在结果上与 random.choice(range(10, 100, 2) 等效。
5.random.choice(sequence)。
sequence 可以使list，tuple，字符串

print random.choice("Python2.7")
print random.choice(["I","love", "you","daisy"])


6.random.shuffle(x[, random])，用于将一个列表中的元素打乱。如:

p = ["test","python", "shuffle","example", "daisy"]
random.shuffle(p)
print p

7.random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。
sample函数不会修改原有序列。

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myslice = random.sample(list, 3)  #从list中随机获取3个元素，作为一个片断返回
print myslice
print mylist #原有序列并没有改变。

"""

import random

print 'random.random():', random.random()
print 'random.uinform(5,10):', random.uniform(5, 10)
print 'random.uinform(10,5):', random.uniform(10, 5)
print 'random.uinform(5,5):', random.uniform(5, 5)
print 'random.randint(5,10):', random.randint(5, 10)
# print 'random.randint(10,5):', random.randint(10, 5)   # 错误：只能小数在前面
print 'random.randint(5,5):', random.randint(5, 5)
print 'random.randrange(10, 100, 2):', random.randrange(10, 100, 2)
print 'random.choice("Python2.7"):', random.choice("Python2.7")
print 'random.choice(["I","love", "you","daisy"]):', random.choice(["I","love", "you","daisy"])

p = ["test","python", "shuffle","example", "daisy"]
random.shuffle(p)
print 'random.shuffle(p):', random.shuffle(p)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print 'random.sample(mylist, 3):', random.sample(mylist, 3)
print 'after random.sample(mylist, 3):', mylist


"""
result:
random.random(): 0.0635703488692
random.uinform(5,10): 6.68689016111
random.uinform(10,5): 5.85245723418
random.uinform(5,5): 5.0
random.randint(5,10): 7
random.randint(5,5): 5
random.randrange(10, 100, 2): 92
random.choice("Python2.7"): n
random.choice(["I","love", "you","daisy"]): daisy
random.shuffle(p): None
random.sample(mylist, 3): [2, 7, 9]
after random.sample(mylist, 3): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
