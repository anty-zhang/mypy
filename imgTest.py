# -*- coding:utf-8 -*-

import sys
import os
import time
from PIL import Image
from cStringIO import StringIO

import urllib2


def test1():
    url = 'http://mmbiz.qpic.cn/mmbiz/57YjMnXvILkS84raPG36ZC6YoAogQK5vvnWZduGBg5HgXGP2ZDibJscUO0cw7GoAWLkVLhus59dVDM66sfwNyNg/0'
    socket = urllib2.urlopen(url)
    data = socket.read()

    # print 'down data is:', data
    img = Image.open(StringIO(data))
    print 'down data img size:', img.size
    '''
    url_file_name = os.path.join(file_path, 'down_img')
    with open(url_file_name, 'wb') as f:
        f.write(data)
    '''
    socket.close()


def test2():
    timeout = 10
    try:
        # urllib2.socket.setdefaulttimeout(timeout)
        # time.sleep(6)
        url = 'http://mmbiz.qpic.cn/mmbiz/57YjMnXvILkS84raPG36ZC6YoAogQK5vvnWZduGBg5HgXGP2ZDibJscUO0cw7GoAWLkVLhus59dVDM66sfwNyNg/0'
        response = urllib2.urlopen(urllib2.Request(url), timeout=timeout)
        # socket.setdefaulttimeout(timeout)
        data = response.read()

        # print 'down data is:', data
        img = Image.open(StringIO(data))
        if img.size[0] <= 800 and img.size[1] <= 100:
            print 'down data img size:', img.size

        response.close()
    except:
        pass

if __name__ == '__main__':
    file_path = os.path.join(os.getcwd(), "photo")
    file_names = os.listdir(file_path)
    print file_names
    '''
    for file in file_names:
        file = os.path.join(file_path, file)
        img = Image.open(file)
        print 'file name:', file, ', size:', img.size
    '''

    test2()


