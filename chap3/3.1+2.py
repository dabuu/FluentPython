# coding:utf-8
"""
@file: 3.1+2.py
@time: 2018/9/30 15:54
@contact: dabuwang
@desc: 3.1 泛映射类型: collections.abc (python 3.3+) || collections (python 2.6~3.2) : Mapping & MutableMapping. 为dict 或类似的类型定义形式接口。
3.2 dict comprehension 字典推导
"""
__author__ = 'dabuwang'

import collections


def collection_abc_test_1():
    """
    只有“可散列”的数据类型才能作用这些映射里的key。
    “可散列”的数据类型是什么？
        '如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需求实现__hash__(),__qe__()方法 [dabu: 是不是__eq__()?]
        如果两个可散列对象是相等的，那么它们的散列值一定是一样的。
        '
    常见的可散列数据类型：
    1. 原子不可变数据类型：str, bytes, 数值型，
    2. frozenset也是可散列，其定义是只能包含 可散列类型。
    3. 元组？ 只有运足包含的所有元素是可散列类型的情况下，它才是可散列的。
    """

    my_dict = {}
    print isinstance(my_dict, collections.MutableMapping)
    print isinstance(my_dict, collections.Mapping)
    print isinstance(my_dict, dict)

    print "====================="

    tt = (1, 2, (30, 40))
    print "%s\n%s" % (tt, hash(tt))

    tf = (1, 2, frozenset([30, 40]))
    print "%s\n%s" % (tf, hash(tf))

    try:
        tl = (1, 2, [30, 40])
        print "%s\n%s" % (tl, hash(tl))
    except TypeError, te:
        print "Warning: type error: %s" % te

    print "====================="

    a = dict(one=1, two=2, three=3)
    b = {'one': 1, "two": 2, "three": 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('three', 3), ('one', 1)])
    e = dict({"two": 2, "three": 3, 'one': 1})
    print a == b == c == d == e


def dict_comp_test_2():
    DIAL_CODES = [
        (86, "China"),
        (1, "Usa"),
        (55, "Brazil"),
        (81, "Japan"),
    ]

    country_code = {country: code for code, country in DIAL_CODES}
    print country_code

    asia_country_code = {code: country.upper() for country, code in country_code.items() if code > 80}
    print asia_country_code


if __name__ == '__main__':
    # collection_abc_test_1()
    dict_comp_test_2()
