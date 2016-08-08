# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    npl = np.array([1, 2, 3, 4, 5, 6])
    # l = [2, 3, 4]
    l = np.array([2, 3, 4])

    print np.setdiff1d(npl, l)
