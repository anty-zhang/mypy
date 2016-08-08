# -*- coding:utf-8 -*-


def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

if __name__ == '__main__':

    for n in fab(5):
        print n
