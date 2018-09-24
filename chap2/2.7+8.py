# coding:utf-8
"""
@file: 2.7+8.py
@time: 2018/9/24 下午7:24
@contact: dabuwang
@desc: 2.7： list.sort vs sorted
2.8 bisect
"""

import bisect


def sorted_test_1():
    """
    list.sort will return None
    sorted will return New list
    ----- same args -----
    1. reverse  (default is False, means 'ASC' )
    2. key (sort func, like max, min,len etc)
    :return:
    """
    fruits = ['grape', 'raspberry', 'apple', 'banana']
    print fruits
    print sorted(fruits)
    print sorted(fruits, reverse=True)
    print sorted(fruits, key=len, reverse=True)
    print fruits
    fruits.sort()
    print fruits


def __grade(score, breakpoints=(60, 70, 80, 90), grades="FDCBA"):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


def bisect_test_1(fn_left):
    """
    bisect
    bisect.bisect == bisect.bisect_right
    :return:
    """
    HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
    NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
    ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'

    if fn_left == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:')
    print('haystack -> %s' % ' '.join('%2d' % n for n in HAYSTACK))
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * '  |'
        print(ROW_FMT.format(needle, position, offset))

    print "===== test grades ====="
    test_scores = [33, 99, 77, 70, 89, 90, 100]
    print test_scores
    print [__grade(score) for score in test_scores]


def bisect_test_2():
    """
    insort : keep the sorted list is always sorted
    :return:
    """
    import random
    SIZE = 7
    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(SIZE*2)
        bisect.insort(my_list, new_item)
        print "%2d ->" % new_item, my_list

if __name__ == '__main__':
    # sorted_test_1()
    # bisect_test_1("left")
    bisect_test_1("")
    # bisect_test_2()
