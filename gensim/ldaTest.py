# -*- coding:utf-8 -*-

"""
    http://blog.csdn.net/whzhcahzxh/article/details/17528261
    http://radimrehurek.com/gensim/tutorial.html
    http://nbviewer.ipython.org/github/wpli/latentmodels/blob/master/gensim_tutorial.ipynb
"""

# gensim包中引用corpora,models, similarities，分别做语料库建立，模型库和相似度比较库
from gensim import corpora, models, similarities

import jieba
import jieba.posseg as pseg


if __name__ == "__main__":
    sentences = ["我喜欢吃土豆", "土豆是个百搭的东西", "我不喜欢今天雾霾的北京"]
    words = []
    for doc in sentences:
        print
        words.append(list(jieba.cut(doc)))
    print words

    # 得到的分词结果构造词典,相当于词袋
    """
        corpora.Dictionary() 返回的数据结构为：词：编号
        例如：
        霾 编号为: 14
        吃 编号为: 0
    """
    dic = corpora.Dictionary(words)
    print 'dic=', dic
    print 'dic.token2id:', dic.token2id

    for word, index in dic.token2id.iteritems():
        print word, "编号为:", str(index)

    # 词典生成好之后，就开始生成语料库了
    """
    为每一个条目按着词典生成预料库，格式如下
    [[(0, 1), (1, 1), (2, 1), (3, 1)],
     [(2, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1)],
     [(1, 1), (3, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1)]]

        # 可序列化到磁盘
        corpora.SvmLightCorpus.serialize('/tmp/corpus.svmlight', corpus)
        corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)
        corpora.LowCorpus.serialize('/tmp/corpus.low', corpus)

        # 从磁盘读取序列化的数据
        corpus = corpora.MmCorpus('/tmp/corpus.mm')
    """
    corpus = [dic.doc2bow(text) for text in words]
    print corpus


    """
    # 做一个TF-IDF变换
    # 可以理解成 将用词频向量表示一句话 变换成为用 词的重要性向量表示一句话
    # （TF-IDF变换：评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降。）
    """
    tfidf = models.TfidfModel(corpus)

    vec = [(0, 1), (4, 1)]
    print tfidf[vec]
    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print doc

    # vec是查询文本向量，比较vec和训练中的三句话相似度
    """
        /usr/lib/python2.7/site-packages/numpy/core/fromnumeric.py:2499:
        VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or
        function instead. To find the rank of a matrix
        see `numpy.linalg.matrix_rank`. VisibleDeprecationWarning)
    """

    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=14)
    sims = index[tfidf[vec]]
    print 'sim:', list(enumerate(sims))



    # 回到tfidf转换，接着训练LSI模型，假定三句话属于2个主题
    # 这就是基于SVD建立的两个主题模型内容
    lsi = models.LsiModel(corpus_tfidf, id2word=dic, num_topics=2)
    lsiout=lsi.print_topics(2)
    print lsiout[0]
    print lsiout[1]

    # 将文章投影到主题空间中
    corpus_lsi = lsi[corpus_tfidf]
    for doc in corpus_lsi:
        print doc

    """
    输出：
        [(0, -0.70861576320682107), (1, 0.1431958007198823)]
        [(0, -0.42764142348481798), (1, -0.88527674470703799)]
        [(0, -0.66124862582594512), (1, 0.4190711252114323)]
     因此第一三两句和主题一相似，第二句和主题二相似
    """

    # 同理做个LDA
    lda = models.LdaModel(corpus_tfidf, id2word=dic, num_topics=2)
    ldaOut = lda.print_topics(2)
    print ldaOut[0]
    print ldaOut[1]
    corpus_lda = lda[corpus_tfidf]
    for doc in corpus_lda:
        print doc

    """
        得到的结果每次都变，给一次的输出：
    0.077*吃 + 0.075*北京 + 0.075*雾 + 0.074*今天 + 0.073*不 + 0.072*霾 + 0.070*喜欢 + 0.068*我 + 0.062*的 + 0.061*土豆
    0.091*吃 + 0.073*搭 + 0.073*土豆 + 0.073*个 + 0.073*是 + 0.072*百 + 0.071*东西 + 0.066*我 + 0.065*喜欢 + 0.059*霾
    [(0, 0.31271095988105352), (1, 0.68728904011894654)]
    [(0, 0.19957991735916861), (1, 0.80042008264083142)]
    [(0, 0.80940337254233863), (1, 0.19059662745766134)]

    第一二句和主题二相似，第三句和主题一相似
    """

    # 输入一句话，查询属于LSI得到的哪个主题类型，先建立索引：
    print '输入一句话，查询属于LSI得到的哪个主题类型'
    print 'query = 雾霾'
    index = similarities.MatrixSimilarity(lsi[corpus])
    query = "雾霾"
    query_bow = dic.doc2bow(list(jieba.cut(query)))
    print query_bow
    query_lsi = lsi[query_bow]
    print query_lsi

    """
    输出:

    [(13, 1), (14, 1)]
    [(0, 0.50670602027401368), (1, -0.3678056037187441)]
    与第一个主题相似
    """

    # 比较和第几句话相似，用LSI得到的索引接着做，并排序输出
    print '比较和第几句话相似，用LSI得到的索引接着做，并排序输出'
    sims = index[query_lsi]
    print 'before sort:', list(enumerate(sims))
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    print 'after sort:', sort_sims
    """
    输出：
    [(0, 0.90161765), (1, -0.10271341), (2, 0.99058259)]
    [(2, 0.99058259), (0, 0.90161765), (1, -0.10271341)]
    可见和第二句话相似度很高，因为只有第二句话出现了雾霾两个词，
    可是惊讶的是和第一句话的相似度也很高，这得益于LSI模型的算法：
    在A和C共现，B和C共现的同时，可以找到A和B的相似度
    """
