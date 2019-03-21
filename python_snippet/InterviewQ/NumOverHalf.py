# coding:utf-8
"""
@file: NumOverHalf.py
@time: 2019/3/21 13:08
@contact: dabuwang
@desc: one list , contain one INT value , which is over half of the list's count
"""
__author__ = 'dabuwang'

import collections


def find_over_half_len_value(alist):
    if not isinstance(alist, collections.Iterable):
        print "input is not a list: %s", repr(alist)
        return None

    flag = 1
    f_value = None
    for v in alist:
        if not isinstance(v, int):
            print "%s is not an INT", repr(v)
            continue

        if f_value == v:
            flag += 1
        else:
            flag -= 1

        if flag == 0:
            f_value = v
            flag = 1

    print "%s find value: %s" % (repr(alist), f_value)


if __name__ == '__main__':
    find_over_half_len_value([1, 1, 2])
    find_over_half_len_value([1, 2, 1, 2, 1])
    find_over_half_len_value([2, 1, 2, 1, 1])
    find_over_half_len_value([1, ])
    find_over_half_len_value([1, 1])
    find_over_half_len_value([2, 2, 1, 1, 1])
    find_over_half_len_value(['a', 2, 2, 1, 1, 1])
    find_over_half_len_value([2, 2, 1, 'a', 1, 1])
    # wrong input, can't get right value
    find_over_half_len_value([1, 1, 2, 2])
    find_over_half_len_value('a1233b')
