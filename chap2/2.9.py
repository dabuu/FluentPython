# coding:utf-8
"""
@file: 2.9.py
@time: 2018/9/24 下午8:32
@contact: dabuwang
@desc: when "list" is NOT first choice
"""

import tempfile
from array import array
from random import random

def array_test_1():
    """
    when the type is specific, array is better choice
    :return:
    """
    floats = array('d', (random() for i in xrange(10**7)))  # 'd' means double type
    print floats[-1]

    test_temp = tempfile.mktemp(prefix="test29_")
    with open(test_temp, 'wb') as fp:
        floats.tofile(fp)

    floats2 = array('d')
    with open(test_temp, 'rb') as fp:
        floats2.fromfile(fp, 10**7)

    print floats2[-1]

def memview_test_2():
    numbers = array('h', [-2, -1, 0, 1, 2])
    numbers = b'abcefg'
    print numbers

    memv = memoryview(numbers)
    print len(memv)
    print memv

    memv_oct = memv.cast('B')
    print memv_oct.tolist()
    memv_oct[5] = 4
    print numbers


if __name__ == '__main__':
    # array_test_1()
    memview_test_2()
