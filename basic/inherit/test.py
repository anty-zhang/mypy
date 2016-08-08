# -*- coding: utf-8 -*-

from basic_similarities import UserSimilarity


class MyClass():
    def __init__(self):
        self.similarity = None

    # protected method
    def _set_similarity(self):
        self.similarity = UserSimilarity(num_best=2)

    def show(self):
        self._set_similarity()
        #父类中定义了__getitem__则调用父类的,如果子类定义了则调用子类的
        print self.similarity[3]

if __name__ == '__main__':
    myc = MyClass()
    myc.show()