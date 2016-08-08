# -*- coding: utf-8 -*-

import warnings


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


# python -W ignore yourscript.py        命令行忽略报警错误
