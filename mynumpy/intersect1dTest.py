# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    source_list = [(2, 4.5), (3, 1.0), (4, 4.0)]
    target_list = [(1, 3.0), (2, 4.0), (3, 3.5), (4, 5.0), (5, 3.0)]
    src = dict(source_list)
    tgt = dict(target_list)

    inter = np.intersect1d(src.keys(), tgt.keys())
    print 'dict src:', src
    print 'dict tgt:', tgt
    print 'inter inter:', inter

    # zip(*): 将values 重组 [(4.5, 1.0, 4.0), (4.0, 3.5, 5.0)]
    common_preferences = zip(*[(src[item], tgt[item]) for item in inter \
            if not np.isnan(src[item]) and not np.isnan(tgt[item])])

    '''
    # error
    temp1 = zip([(src[item], tgt[item]) for item in inter \
            if not np.isnan(src[item]) and not np.isnan(tgt[item])])
    '''

    print common_preferences
    print np.asarray([common_preferences[0]]), np.asarray([common_preferences[1]])
    print np.array([common_preferences[0]]), np.asarray([common_preferences[1]])
