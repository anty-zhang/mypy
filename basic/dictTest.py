# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d1 = {2: 4.5, 3: 1.0, 4: 4.0}
    d2 = {1: 3.0, 2: 4.0, 3: 3.5, 4: 5.0, 5: 3.0}

    inter = set(d1) & set(d2)

    print inter
