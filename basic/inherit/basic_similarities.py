# -*- coding:utf-8 -*-

from base import BaseSimilarity


class UserSimilarity(BaseSimilarity):
    def __init__(self, num_best=None):
        BaseSimilarity.__init__(self, num_best)

    def get_similarity(self, source_id, target_id):
        print 'inherite class get_similarity:', source_id, ', ', target_id

    def get_similarities(self, source_id):
        print 'inherite class get_similarities:', source_id

    '''
    def __getitem__(self, source_id):
        print 'inherite class __getitem__:', source_id
        return source_id
    '''

