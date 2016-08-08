# -*- coding: utf-8 -*-

"""
将字典转为对象方式调用

AttributeDict 为字典对象
"""


class AttributeDict(dict):
    def __getattr__(self, attr):
        print '__getattr__', attr
        return self[attr]

    def __setattr__(self, attr, value):
        print '__setattr__ attr: ', attr, ', value: ', value
        self[attr] = value


if __name__ == '__main__':
    d = AttributeDict()
    d.update({'it': ["jacket", "necktie", "trousers"], 't123': 223, })

    print d.it
    print d.t123