# -*- coding:utf-8 -*-

"""
    np.arange(起始值,结束值,步长)
    np.linspace(起始值,结束值,元素个数)  --->等差数列
    np.flat  --->转化为一维数组
"""


import numpy as np
if __name__ == '__main__':
    arr = np.arange(1, 7).reshape(2, 3)
    print arr

    lin = np.linspace(0, 2, 9)
    print 'lin:', lin

    print '===test flat==='
    print 'arr.flat[3]:', arr.flat[3]
    print 'arr.T.flat[3]=', arr.T.flat[3]
    print 'type(arr.flat):', type(arr.flat)
    arr.flat = 3
    print 'arr.flat=3:', arr
    arr.flat[[1, 4]] = 1     # 将第1和4元素赋值为1
    print 'arr.flat[[1, 4]] = 1:', arr

    print '===test flatten==='
    a = np.array([[1, 2, 5], [3, 4, 6]])
    print a.flatten("C")    # row-major  default
    print a.flatten("F")    # column-major

    """
        [[1 2 3]
        [4 5 6]]
        lin: [ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ]
        ===test flat===
        arr.flat[3]: 4
        arr.T.flat[3]= 5
        type(arr.flat): <type 'numpy.flatiter'>
        arr.flat=3: [[3 3 3]
                    [3 3 3]]
        arr.flat[[1, 4]] = 1: [[3 1 3]
                                [3 1 3]]
     """
