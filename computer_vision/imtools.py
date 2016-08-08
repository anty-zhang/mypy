# -*- coding: utf-8 -*-

import os


def get_imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(".jpg")]


if __name__ == '__main__':
    path = "/home/andy/Documents/documents/python/computer_vision/image"
    im_list = get_imlist(path)
    print 'im_list:', im_list