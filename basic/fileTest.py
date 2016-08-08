# -*- coding: utf-8 -*-
import sys


def file_handle(file_name):
    """
    with 和iter使用
    """
    with open(file_name) as fp:
        for line in iter(fp.readline, ''):
            print 'line: ', line

if __name__ == '__main__':
    file = sys.argv[1]
    file_handle(file)