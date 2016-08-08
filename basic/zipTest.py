# -*- coding:utf-8 -*-
import numpy as np

if __name__ == '__main__':
    l = [(1, np.array([[0.66284898]])),
         (2, np.array([[0.92447345]])),
         (3, np.array([[0.89340515]])),
         (4, np.array([[0.99124071]])),
         (5, np.array([[1.]])),
         (6, np.array([[0.38124643]])),
         (7, np.array([[-1.]]))]

    print 'l:', l

    userId, preferences = zip(*l)

    print 'userID:', userId, ' ,preferences:', preferences

    l = [1, 2, 3]
    al = np.array(l)
    print al.flatten()


    print 7 * 24 * 60 * 60