# -*- coding: utf-8 -*-


class MyException(Exception):
    pass

try:
    raise MyException({1:22, 2: 333})
except Exception, e:
    raise MyException("get_bucket error(%s)." % e)