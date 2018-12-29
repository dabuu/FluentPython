# coding:utf-8
"""
@file: reference_usage.py
@time: 2018/11/21 9:48
@contact: dabuwang
@desc: todo
"""
__author__ = 'dabuwang'

def test_list_as_reference():
    t = "aa bb cc".split()
    print "t_init", t
    __handle_list(t)
    print "t_handled",t

    pass

def __handle_list(t_list):
    t_list.insert(0,'xx')
    print "t_list", t_list

if __name__ == '__main__':
    test_list_as_reference()