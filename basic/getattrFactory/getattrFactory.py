# -*- coding: utf-8 -*-


""""
getattr 实现工厂模式
"""

import statsout


def output(data, format="text"):
    output_function = getattr(statsout, "statsout_%s" %format)
    return output_function(data)


if __name__ == '__main__':
    output('test1', 'html')
    output('test2', 'xml')