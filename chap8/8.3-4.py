# coding:utf-8
"""
@file: 8.3-4.py.py
@time: 6/13/2019 10:22 PM
@contact: dabuwang
"""

def section8_3_0x01():
    """
    list() or [:] 默认是浅拷贝
    http://www.pythontutor.com/  python 交互动画
    :return:
    """
    l1 = [3, [55, 44], (7, 8, 9)]
    l2 = list(l1)   # l1[:]
    print "l2 == l1", l2 == l1
    print "l2 is l1", l2 is l1
    print "l2[1] is l1[1]", l2[1] is l1[1]
    print "l2's value is same as l1, but l2 is not l1."
    print "\033[0;31;47m*Notice*: l1[1] is l2[1], which would cause bugs!\033[0m"

    print "-"*20
    print "l2: ", l2
    l1.append(100)
    print "l1.append(100): ", l1
    l1[1].remove(55)
    print "l1[1].remove(55): ", l1
    print "l2 now:", l2

    print "-" * 30
    print "id(l1[1]),id(l2[1])", id(l1[1]), id(l2[1])
    l2[1] += [33,22]
    print "l2[1] += [33,22], id(l1[1]),id(l2[1]):  ", id(l1[1]), id(l2[1])
    print "l2[1] += [33,22], l1, l2:  ", l1, l2

    print "id(l1[2]),id(l2[2])", id(l1[2]), id(l2[2])
    l2[2] += (10, 11)
    print " l2[2] += (10, 11), id(l1[2]),id(l2[2]):  ", id(l1[2]), id(l2[2])
    print "l2[2] += (10, 11), l1, l2:  ", l1, l2
    print "\033[0;31;47m*Notice*: list1 += list2, the id(list1) is NOT change! But it will FAIL when '+=' using at tuple! Details: chap2:2.5+6.py\033[0m"

def section8_3_0x02():
    pass

if __name__ == '__main__':
    section8_3_0x01()