# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas
# d = pandas.read_table("global2000.txt", sep = ",")
# c = d["\tCountry"]
# #print c
# vc = d["\tCountry"].value_counts()
# print "-------------"
# for x, y in vc.iteritems():
#     print x, y
# print vc.keys()
# label = list(set(d["\tCountry"]))
# expl = (0.05 , 0)
# plt.pie(vc[:10], labels = vc[:10].keys(), autopct="%5.2f%%", pctdistance=0.6,
# shadow=True, labeldistance=1.1, startangle=None, radius=None)
# plt.show()


def gcd(a, b):
    if a < b:   #调换位置，使得a > b，以便a % b取余
        a, b = b, a
    y = a % b
    if y == 0:
        return b
    else:
        a, b = b, y
        return gcd(a, b)


def video_size_pipe():
    all_dict = {'all': 0}
    df = pandas.read_table("video_size.txt", sep=":", names=['w', 'h', 'k'])
    for index, row in df.iterrows():
        w = row['w']
        h = row['h']
        div = gcd(w, h)
        k = "%d/%d" % (w/div, h/div)
        all_dict[k] = all_dict.get(k, 0) + 1
        all_dict['all'] = all_dict.get('all', 0) + 1

    # sort_all_dict = sorted(all_dict.iteritems(), key=lambda (k, v): v, reverse=True)[:11]
    sort_all_dict = sorted(all_dict.iteritems(), key=lambda (k, v): v, reverse=True)

    print sort_all_dict
    all_count = 0.0
    for k, v in sort_all_dict:
        if k == 'all':
            all_count = float(v)
            continue
        print k, round(float(v)/float(all_count), 3)


if __name__ == '__main__':
    video_size_pipe()