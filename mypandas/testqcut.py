# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os


def build_data(fn):
    lines = []
    if os.path.exists(fn):
        with open(fn, "rb") as f:
            text = f.read()
            lines = text.split("\n")
    lines = [float(l)/1000000.0 for l in lines if l]
    print lines
    return lines


def main(fn):
    d = {}
    data = build_data(fn)
    # qd = pd.qcut(data, 10, labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    qd = pd.qcut(data, 10)
    print qd
    res = qd.value_counts()
    print res
    all_count = res.sum()
    # print qd.categories
    # count = 0
    # for t in qd:
    #     count += 1
    #     if t in d:
    #         d[t] += 1
    #     else:
    #         d[t] = 1
    # d = sorted(d.iteritems(), key=lambda (k, v): k)
    # for k, v in d:
    #     print 'k: ', k, ', ratio: ', round(float(v) / count, 3) * 100


    # df = pd.DataFrame(d.values(), d.keys())
    # print df
    # plt.figure()
    # df.plot.bar()


if __name__ == '__main__':
    main(sys.argv[1])