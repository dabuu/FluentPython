# coding:utf-8
"""
@file: 3.5+6.py
@time: 2018/9/30 17:49
@contact: dabuwang
@desc: 3.5 字典的变种： OrderedDict, ChainMap (python3.3+, not show case in this .py), Counter, UserDict

"""
__author__ = 'dabuwang'

import collections

def test_other_dicts_1():
    ct = collections.Counter('abababrcdra')
    print ct
    print "".join([x for x in ct.elements()])
    ct.update("dddcaaaa")
    print ct
    print "".join([x for x in ct.elements()])
    print ct.most_common(2)


def test_userDict_2():
    """
    due to "UserDict" is no available in python2.7, so only paste the class code in book
    https://docs.python.org/3/library/collections.html?highlight=collections#collections.UserDict
    :return:
    """
    """
    class StrKeyDict(collections.UserDict):

        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]

        def __contains__(self, key):
            return str(key) in self.data

        def __setitem__(self, key, item):
            self.data[str(key)] = item  
    """
    pass


if __name__ == '__main__':
    test_other_dicts_1()