# -*- coding: utf-8 -*-

from recsys.algorithm.factorize import SVD
svd = SVD()

# 1. Load Movielens dataset:
svd.load_data(filename='/home/andy/xx/recommend/ratings.dat',
            sep='::',
            format={'col':0, 'row':1, 'value':2, 'ids': int})


# 2. Compute Singular Value Decomposition (SVD), M=U Sigma V^t:
k = 100
svd.compute(k=k,
            min_values=10,
            pre_normalize=None,
            mean_center=True,
            post_normalize=True,
            savefile='/tmp/movielens')

# 3. Get similarity between two movies:
ITEMID1 = 1    # Toy Story (1995)
ITEMID2 = 2355 # A bug's life (1998)

print svd.similarity(ITEMID1, ITEMID2)
# 0.67706936677315799


"""

# 4. Get movies similar to Toy Story:
svd.similar(ITEMID1)


# 5. Predict the rating a user (USERID) would give to a movie (ITEMID):
MIN_RATING = 0.0
MAX_RATING = 5.0
ITEMID = 1
USERID = 1

svd.predict(ITEMID, USERID, MIN_RATING, MAX_RATING)
# Predicted value 5.0

svd.get_matrix().value(ITEMID, USERID)
# Real value 5.0


# 6. Recommend (non-rated) movies to a user:
svd.recommend(USERID, is_row=False) #cols are users and rows are items, thus we set is_row=False


# 7. Which users should see Toy Story? (e.g. which users -that have not rated Toy Story- would give it a high rating?)







"""



