# -*- coding: utf-8 -*-

import json


def swap(a, b):
    c = a
    a = b
    b = c

if __name__ == "__main__":
    # file_name = "/home/andy/test_json.txt"
    # with open (file_name, "rb") as f:
    #     text = f.read()
    #
    # print json.loads(text)
    
    a = 10
    b = 20
    swap(a, b)
    
    print a, b
    
    