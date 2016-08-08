# -*- coding: utf-8 -*-
"""
iterable：是可迭代类型;
cmp：用于比较的函数，比较什么由key决定,有默认值，迭代集合中的一项;
key：用列表元素的某个属性和函数进行作为关键字，有默认值，迭代集合中的一项;
reverse：排序规则. reverse = True 或者 reverse = False，有默认值。
返回值：是一个经过排序的可迭代类型，与iterable一样。

注；一般来说，cmp和key可以使用lambda表达式。

sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表。
注：效率key>cmp(key比cmp快)


"""

a = [1, 2, 5, 4]

print sorted(a)
print sorted(a, reverse=True)
print a

print a.sort()
print a


print '=============================='
from operator import itemgetter


mydict = { 'a1': (1,6),
          'a2': (10,2),
          'a3': (5,3),
          'a4': (1,2),
          'a5': (3,9),
          'a6': (9,7) }

# sort by first element of the value tuple: WORKS
print sorted(mydict.iteritems(), key=lambda (k, v): v[0])

# sort by second element of the value tuple: WORKS
print sorted(mydict.iteritems(), key=lambda (k, v): v[1])


# THIS is what I can't get working:
def cmpRatio(**kwargs):
   # sx = float(x/y)
   # sy = float(y/x)
   # return sx < sy
   return 1

# sort by sum of the elements in the value tuple: DOES NOT WORK
# print sorted(mydict.iteritems(), key=lambda (k,v): v, cmp=cmpRatio)
# print sorted(mydict.iteritems(), key=itemgetter(1), cmp=cmpRatio)
print '-----------------------------'
print sorted(mydict.iteritems(), cmp=cmpRatio)

