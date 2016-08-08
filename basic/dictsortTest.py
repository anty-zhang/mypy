# -*- coding: utf-8 -*-

import itertools

mykeys = ['b', 'a', 'c']
myvalues = ['bbb', 'aaa', 'cccc']


d = dict(itertools.izip(mykeys, myvalues))

print 'd=', d


def sortDictValue(kdict):
    keys = kdict.keys()
    print 'before sort:', keys
    keys.sort()
    print 'after sort:', keys
    return map(kdict.get, keys)

print sortDictValue(d)