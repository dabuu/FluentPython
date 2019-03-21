# coding:utf-8
"""
@file: FindSecMax.py
@time: 2019/3/21 15:36
@contact: dabuwang
@desc: find the Second max value from INT list
"""
__author__ = 'dabuwang'


def find_sec_max(alist):
    print "=" * 10 + "> find sec value: %s" % repr(alist)
    x, y = None, None
    if len(alist) < 1:
        return None

    for i in alist:
        if not isinstance(i, int):
            print "not int", repr(i)
            continue
        if x is None:
            x = i

        if i > x:
            x, y = i, x
        elif x > i > y:
            y = i
    print "sec value:", repr(y)
    return y


if __name__ == '__main__':
    find_sec_max([1, 2, 3])  # 2
    find_sec_max([2, 3, 3])  # 2
    find_sec_max([3, 3, 3])  # none
    find_sec_max([3, 2, 3, 1])  # 2
    find_sec_max([3, 2])  # 2
    find_sec_max([1])  # none
    find_sec_max([3, 2, 3, 111111111111111111])  # 2
    find_sec_max(['@', 3, 2, 1, 'a'])  # 2
