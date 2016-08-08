# -*- coding: utf-8 -*-
##################################################################################
# python 多继承
##################################################################################


class A(object):
    def __init__(self):
        print 'A __init__'
        super(A, self).__init__()
        print 'leave A'


class C(object):
    def __init__(self):
        print 'C __init__'
        super(C, self).__init__()
        print 'leave C'


class B(A, C):
    def __init__(self):
        print 'B __init__'
        super(B, self).__init__()
        print 'leave B'


class D(B):
    def __init__(self):
        print 'D __init__'
        super(D, self).__init__()
        print 'leave D'
if __name__ == '__main__':
    D()