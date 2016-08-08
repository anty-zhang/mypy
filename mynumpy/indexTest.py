# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    l1 = [1,  2,  3,  4,  5,  6,  7,  8,  9, 10]
    l2 = [10,  20,  30,  40,  50,  60,  70,  80,  90, 100]
    l3 = [100,  200,  300,  400,  500,  600,  700,  800,  900, 1000]

    nl = np.array([l1, l2, l3])

    # index_nl = np.array([[], [1, 2]])
    index_nl = np.array([1, 2])
    print nl[index_nl, 5]
