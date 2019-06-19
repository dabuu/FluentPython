# coding:utf-8
"""
@file: AndOr.py
@time: 2019/6/19 13:22
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'


def and_vs_or():
    print "1 == 1 and 'a' or 'b':\t", 1 == 1 and 'a' or 'b'
    print "2 == 1 and 'a' or 'b':\t", 2 == 1 and 'a' or 'b'

    print "-" * 20
    print "repr(None and 'a'):\t", repr(None and 'a')
    print "repr(None or 'b'):\t", repr(None or 'b')


if __name__ == '__main__':
    and_vs_or()
