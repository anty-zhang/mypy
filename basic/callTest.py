# -*- coding: utf-8 -*-

"""
 Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。
"""


class Animal(object):
    def __init__(self, name, legs):
        print '__init__ start'
        self.name = name
        self.legs = legs
        self.stomach = []
        print '__init__ end'

    def __call__(self, food):
        print '__call__ start'
        self.stomach.append(food)
        print '__call__ end'

    def poop(self):
        print 'poop start'
        if len(self.stomach) > 0:
            return self.stomach.pop(0)
        print 'poop end'

    def __str__(self):
        print '__str__'
        return 'A animal named %s' % (self.name)


if __name__ == '__main__':
    cow = Animal('king', 4)    #We make a cow
    dog = Animal('flopp', 4)   #We can make many animals

    print 'We have 2 animales a cow name %s and dog named %s,both have %s legs' % (cow.name, dog.name, cow.legs)
    print cow                  #here __str__ metod work


    #We give food to cow
    cow('gras')
    print cow.stomach

    print '---------------------------------------------------------'
    #We give food to dog
    dog('bone')
    dog('beef')
    print dog.stomach

    print '---------------------------------------------------------'

    #What comes inn most come out
    print cow.poop()
    print cow.stomach  #Empty stomach

