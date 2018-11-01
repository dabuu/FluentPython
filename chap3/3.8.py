# coding:utf-8
"""
@file: 3.8.py
@time: 2018/10/9 16:25
@contact: dabuwang
@desc: about "SET"
"""
__author__ = 'dabuwang'


def set_definition_test_1():
    l = ['ss', 'ss', 'ss', 'aa']
    s = set(l)
    print "set(l) is ", s
    print "list(s) is ", list(s)
    try:
        print s[0]
    except TypeError, te:
        print "warning: s[0]: %s" % te

    print "for s is below:"
    for x in s:
        print x

    sd = {1, 2, 3, 4, 4, 1}
    print "set definition sd:", sd
    print "set type sd:", type(sd)
    sd2 = {0,1}
    print "sd2:", sd2
    for _ in range(len(sd2)):
        sd2.pop()
        print "sd2 pop one:", sd2
    print "empty sd2:", sd2


def set_operation_test_2():
    s1 = {1,2,3,4,5,6,7,8,9}
    s2 = {2,3,4,5,0,-1}

    union_set= len(s2 | s1)
    intersection_set = len(s2 & s1)
    diff_set2 = len(s2 -s1)
    diff_set1 = len(s1 -s2)

    print union_set
    print intersection_set
    print diff_set2
    print diff_set1

def set_diss_test_3():
    """
    反编译字节码，用2.7返回值 跟书中的不一致，觉得这种写法只是两个string的字节码。后续研究一下 dis的用法 todo
    :return:
    """
    from dis import dis
    dis('{1}')
    print "========="
    dis('set({1})')

def set_comprehension_test_4():
    """

    :return:
    """
    from unicodedata import name
    # python 2.7环境 按照书中格式 会提示错误： TypeError: name() argument 1 must be unicode, not str
    # sign_unicodes = {chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')}

    # change str to unicode
    sign_unicodes = {chr(i) for i in range(32,128) if 'SIGN' in name(chr(i).decode(), u'')}
    print sign_unicodes

if __name__ == '__main__':
    # set_definition_test_1()
    # set_operation_test_2()
    # set_diss_test_3()
    set_comprehension_test_4()
