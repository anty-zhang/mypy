# -*- coding: utf-8 -*-
import numpy as np

if __name__ == '__main__':
    all_sims = [(1, np.array([[0.66284898]])),
                (2, np.array([[0.92447345]])),
                (3, np.array([[0.89340515]])),
                (4, np.array([[0.99124071]])),
                (5, 1.0),
                (6, np.array([[0.38124643]])),
                (7, np.array([[-1.]]))]
    '''
    all_sims = [(1, np.array([[0.66284898]])),
                (2, np.array([[0.92447345]])),
                (3, np.array([[0.89340515]])),
                (4, np.array([[0.99124071]])),
                (5, 1.0),
                (6, np.array([[0.38124643]])),
                (7, np.array([[-1.]])),
                (8, np.nan)]    # np.nan 不进行排序
    '''

    item_ids, preferences = zip(*all_sims)
    print 'item_ids:', item_ids
    print 'preferences:', preferences
    item_ids = np.array(item_ids).flatten()
    preferences = np.array(preferences).flatten()
    print 'flatten item_ids:', item_ids
    print 'flatten preferences:', preferences

    sorted_prefs = np.argsort(preferences)  # -负号表示降序排序,返回数组下标
    print 'sorted_prefs:', sorted_prefs

    tops = zip(item_ids[sorted_prefs], preferences[sorted_prefs])
    print 'tops:', tops
    """
    item_ids: (1, 2, 3, 4, 5, 6, 7)
    preferences: (array([[ 0.66284898]]), array([[ 0.92447345]]), array([[ 0.89340515]]), array([[ 0.99124071]]), 1.0, array([[ 0.38124643]]), array([[-1.]]))
    flatten item_ids: [1 2 3 4 5 6 7]
    flatten preferences: [array([[ 0.66284898]]) array([[ 0.92447345]]) array([[ 0.89340515]])
     array([[ 0.99124071]]) 1.0 array([[ 0.38124643]]) array([[-1.]])]
    sorted_prefs: [4 3 1 2 0 5 6]
    tops: [(5, 1.0), (4, array([[ 0.99124071]])), (2, array([[ 0.92447345]])), (3, array([[ 0.89340515]])), (1, array([[ 0.66284898]])), (6, array([[ 0.38124643]])), (7, array([[-1.]]))]
    """
