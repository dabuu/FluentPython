# coding:utf-8
"""
@file: 3.5+6.py
@time: 2018/9/30 17:49
@contact: dabuwang
@desc: 3.5 字典的变种： OrderedDict, ChainMap (python3.3+, not show case in this file), Counter, UserDict

"""
__author__ = 'dabuwang'

import collections

def test_other_dicts():
    ct = collections.Counter('abababrcdra')
    print ct
    print "".join([x for x in ct.elements()])
    ct.update("dddcaaaa")
    print ct
    print "".join([x for x in ct.elements()])
    print ct.most_common(2)


if __name__ == '__main__':
    test_other_dicts()