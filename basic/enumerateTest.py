#!/usr/bin/env python
# encoding: utf-8

# enumerate 使用场景：对一个列表或者数组既要遍历索引又要遍历元素时使用
# 例如：
#     比如：
# for index,value in enumerate(list):
#       print index,value
# 当然也可以
# for i in range(0,len(list)):
#       print i,list[i]
# enumerate 的参数为可遍历的变量，如字符串，列表等;返回值为enumerate类

# 遍历字符串实例
import string

s = string.ascii_lowercase
e = enumerate(s)

print '遍历字符串实'
print 's is:', s
print 'list(e) is:', list(e)


# 遍历列表实例
name_list = ['zhangsan', 'lisi', 'mayun']
for index,item in enumerate(name_list):
    name_list[index] = "%d:%s" % (index, item)

print name_list
name_list = ['zhangsan', 'lisi', 'mayun']

# 更简介的编码方式
print ["%d:%s" % (index,item) for index,item in enumerate(name_list)]
