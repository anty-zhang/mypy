# -*- coding:utf-8 -*-

#测试父类和子类中__getitem__调用方法


class BaseSimilarity(object):
    def __init__(self, num_best=None):
        self._set_num_best(num_best)

    def _set_num_best(self, num_best):
        self.num_best = num_best

    def get_similarity(self, source_id, target_id):
        raise NotImplementedError("cannot instantiate Abstract Base Class")

    def get_similarities(self, source_id):
        raise NotImplementedError("cannot instantiate Abstract Base Class")

    def __getitem__(self, source_id):

        print 'base class __getitem__ source_id:', source_id
        return source_id