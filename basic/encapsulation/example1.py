# -*- coding: utf-8 -*-
##################################################################################
# python封装
##################################################################################

"""
1. __repr__ 和__str__区别
    __repr__的目标是准确性
    __str__的目标是可读性
    容器的__str__使用包含了对象的__repr__

    内建函数str()和repr() (representation，表达，表示)或反引号操作符（``）可以方便地以字符串的方式获取对象的内容
    、类型、数值属性等信息。str()函数得到的字符串可读性好（故被print调用），而repr()函数得到的字符串通常可以用来
    重新获得该对象，通常情况下 obj==eval(repr(obj)) 这个等式是成立的。这两个函数接受一个对象作为其参数，
    返回适当的字符串。

    事实上repr()和``做一样的事情，返回一个对象的“官方”字符串表示。其结果绝大多数情况下（不是所有）可以通过求值运算
    （内建函数eval()）重新得到该对象。
    tr()则不同，它生成一个对象的可读性好的字符串表示，结果通常无法用eval()求值，但适合print输出。

    for example
    # >>> s1 = "Hello,kitty\n"
    # >>> c = str(s1)
    # >>> print c
        Hello,kitty

    # >>> b = repr(s1)
    # >>> print b
        'Hello,kitty\n'


2.super
详解：http://blog.csdn.net/johnsonguo/article/details/585193
super 是用来解决多重继承问题的。
直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、
重复调用（钻石继承）等种种问题。总之前人留下的经验就是：保持一致性。要不全部用类名调用父类，
要不就全部用 super，不要一半一半。
"""

import os


class FFMpegError(Exception):
    pass


class FFMpegConverError(Exception):
    def __init__(self, message, cmd, output, details=None, pid=0):
        super(FFMpegConverError, self).__init__(message)
        self.cmd = cmd
        self.output = output
        self.details = details
        self.pid = pid

    def __repr__(self):
        print '================repr-----------------'
        error = self.details if self.details else self.message
        return '<FFMpegConvertError error="%s", pid=%s, cmd="%s">' \
               % (error, self.pid, self.cmd)

    def __str__(self):
        print '=============str++++++++++++++++++++'
        return self.__repr__()


class MediaFormatInfo(object):
    def __init__(self):
        self.format = None
        self.fullname = None
        self.bitrate = None
        self.duration = None
        self.filesize = None

    def parse_ffprobe(self, key, val):
        """
        Parse raw ffprobe output (key=value).
        """
        if key == 'format_name':
            self.format = val
        elif key == 'format_long_name':
            self.fullname = val
        elif key == 'bit_rate':
            self.bitrate = ''
        elif key == 'duration':
            self.duration = ''
        elif key == 'size':
            self.size = ''

    def __repr__(self):
        print '==========debug MediaFormatInfo __repr__ here'
        if self.duration is None:
            return 'MediaFormatInfo(format=%s)' % self.format
        return 'MediaFormatInfo(format=%s, duration=%.2f)' % (self.format,
                                                              self.duration)


class MediaInfo(object):
    def __init__(self):
        self.format = MediaFormatInfo()
        self.myrepr = None

    def __repr__(self):
        # __repr__ 返回类对象时的内容
        print '=====my debug MediaInfo __repr__ here'
        return 'MediaInfo(format=%s, streams=%s)' % repr(self.format)


class FFMpeg(object):
    def __init__(self, ffmpeg_path=None):
        self.ffmpeg_path = ffmpeg_path

    def testFFMpegError(self):
        if not os.path.exists(self.ffmpeg_path):
            # raise FFMpegError("ffmpeg binary not found:" + self.ffmpeg_path)
            raise FFMpegError("ffmpeg binary not found:%s" % self.ffmpeg_path)

    def testFFMpegConvertError(self):
        raise FFMpegConverError("ncoding error", 'ffmpeg -i input.mp4',
                                'total output', 'test', 1000)

    def testREPR(self):
        info = MediaInfo()
        # print info.format.format
        print info    # 只有返回类的对象时才返回此类中__repr__函数中的信息


if __name__ == '__main__':
    ffmpeg = FFMpeg('/usr/bin/ffmpegg')
    # ffmpeg.testFFMpegError()
    # ffmpeg.testFFMpegConvertError()
    ffmpeg.testREPR()

