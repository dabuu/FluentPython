# coding:utf-8
"""
@file: 2.2.py
@time: 2018/8/17 18:19
@contact: dabuwang
"""
__author__ = 'dabuwang'

symbols = '$%&^#()!@'  # £$¤¥¨ª'#￥¢¤£ÿ'


def list_comprehension():
    for y in symbols:
        print ord(y)

    print "========"
    codes = [ord(x) for x in symbols]
    print codes


def list_comprehension_same_value():
    x = "ABC"
    xlist = [x for x in 'ABC']
    print "x: %s, which SHOULD be ABC, python3.x NOT repo" % x
    print "l:%s" % xlist


def list_comprehension_vs_map_filter():
    beyond_ascii_1 = [ord(x) for x in symbols if ord(x) > 40]
    print beyond_ascii_1

    beyond_ascii_2 = filter(lambda c: c > 40, map(ord, symbols))
    print beyond_ascii_2


def list_comprehension_cartesian_product():
    colors = "black white".split()
    sizes = "S M X".split()

    t_shirts = [(color, size) for color in colors for size in sizes]  # same as for & for
    print t_shirts
    t_shirts = [(color, size) for size in sizes for color in colors]
    print t_shirts


def list_comprehension_generator():
    print (ord(s) for s in symbols)
    print [ord(s) for s in symbols]
    print tuple(ord(s) for s in symbols)

    import array
    print array.array('I', (ord(s) for s in symbols))


def test():
    # list_comprehension()
    # list_comprehension_same_value()
    # list_comprehension_vs_map_filter()
    # list_comprehension_cartesian_product()
    list_comprehension_generator()


if __name__ == '__main__':
    test()
