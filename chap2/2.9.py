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
import numpy


def array_test_1():
    """
    when the type is specific, array is better choice
    :return:
    """
    floats = array('d', (random() for i in xrange(10 ** 7)))  # 'd' means double type
    print floats[-1]

    test_temp = tempfile.mktemp(prefix="test29_")
    with open(test_temp, 'wb') as fp:
        floats.tofile(fp)

    floats2 = array('d')
    with open(test_temp, 'rb') as fp:
        floats2.fromfile(fp, 10 ** 7)

    print floats2[-1]


def memview_test_2():
    """
    the example code (memoryview.cast) should run under python3.3+ in the book. https://docs.python.org/3.6/library/stdtypes.html?highlight=memoryview#memoryview.cast
    so here i just write mv usage example in 2.7 online doc: https://docs.python.org/2.7/library/stdtypes.html?highlight=memoryview#memoryview-type
    书中对memoryview的解释还是 需要粘贴一下的：
    memoryview 是一个内置类，它能让用户在不复制内容的情况下操作同一个数组的不同切片。
    “内存视图其实是泛化和去数学化的 NumPy 数组。它让你在不需要复制内容的前提下，在数据结构之间共享内存。其中数据结构可以是任何形式，比如 PIL 图片、SQLite 数据库和 NumPy 的数组，等等。这个功能在处理大型数据集合的时候非常重要。”
    memoryview.cast 的概念跟数组模块类似，能用不同的方式读写同一块内存数据，而且内容字节不会随意移动。
    memoryview.cast 会把同一块内存里的内容打包成一个全新的 memoryview 对象给你。
    :return:
    """
    data = bytearray('asdfg')
    print data

    mv = memoryview(data)
    print mv
    print len(mv)
    print mv[0]
    print mv.readonly

    mv[0] = 'z'
    print data
    try:
        mv[2] = 'changelength'
    except ValueError, ve:
        print "Warning: should throw error: %s" % ve


def np_sp_test_3():
    """
    numpy 多维同质数组和矩阵
    scipy 线性代数 数值积分 统计学
    :return:
    """
    np_array = numpy.arange(12)
    print np_array
    print type(np_array)
    print np_array.shape

    np_array.shape = 3, 4
    print np_array
    print np_array[2]
    print np_array[2, 1]
    print np_array[:, 1]  # print the column which index = 1
    print np_array.transpose()  # exchange the line and column

    print "===================="
    floats = [str(random()) + '\n' for i in xrange(10)]
    print floats[-3:]
    test_temp = tempfile.mktemp(prefix="test29_3_")
    with open(test_temp, 'w') as fp:
        fp.writelines(floats)

    np_floats = numpy.loadtxt(test_temp)
    print np_floats[-3:]

    np_floats *= 0.5
    print np_floats[-3:]

    ## below is only work for python 3.3+
    # from time import perf_counter as pc
    # t0 = pc(); np_floats /= 3; pc() - t0;
    test_np_temp = tempfile.mktemp(prefix="test29_3_")
    numpy.save(test_np_temp, np_floats)  # numpy.save file to "xx.npy", which could be loaded by "numpy.load"

    np_floats2 = numpy.load(test_np_temp + ".npy", 'r+')
    np_floats2 *= 6
    print np_floats2[-3:]


def deque_test_4():
    """
    collections.deque 类（双向队列）是一个"线程安全"(原子操作)、可以快速从两端添加或者删除元素的数据类型。
    优点： 从两边的操作有优化速度很快
    缺点： 尽量不操作中间元素
    :return:
    """
    from collections import deque
    dq = deque(range(10), maxlen=10)
    print dq

    dq.rotate(3)
    print dq

    dq.rotate(-4)
    print dq

    dq.appendleft(-1)
    print dq

    dq.append(100)
    print dq

    dq.extend([200, 201])
    print dq

    # *notice*, the left result is reversed, LIKE THIS "deque([305, 304, 303, 3, 4, 5, 6, 7, 8, 9], maxlen=10)"
    dq.extendleft([303, 304, 305])
    print dq


if __name__ == '__main__':
    # array_test_1()
    # memview_test_2()
    # np_sp_test_3()
    deque_test_4()
